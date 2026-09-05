import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
embeddings = OpenAIEmbeddings(
    model=os.getenv("OPENAI_EMBEDDING_MODEL"),
    dimensions=320
)


animals_docs = [
    "The lion is a large wild animal known as the king of the jungle. It has a strong body, sharp claws, and powerful teeth. Male lions usually have a thick mane around their heads. Lions live mainly in grasslands and savannas of Africa, with a small population in India. They live in groups called prides and often hunt together. Lions are carnivores and mainly eat animals such as zebras, buffaloes, and antelopes.",
    "The elephant is the largest land animal in the world. It has a long trunk, large ears, strong legs, and two tusks. Elephants use their trunks to breathe, drink water, pick up food, and communicate. They are intelligent and social animals that usually live in family groups. Elephants mainly eat grass, leaves, fruits, bark, and other plants. They are found mainly in Africa and Asia and play an important role in maintaining their ecosystems.",
    "The tiger is a powerful wild cat famous for its orange coat and black stripes. It is mainly found in parts of Asia, including India, Nepal, Bangladesh, and Russia. Tigers are excellent hunters and usually hunt alone rather than in groups. They eat animals such as deer, wild boar, and other mammals. Tigers are also strong swimmers and can cross rivers and lakes easily. They are endangered because of habitat loss, illegal hunting, and conflicts with humans.",
    "The giraffe is the tallest land animal in the world. It is easily recognized by its very long neck, long legs, and unique spotted coat. Giraffes use their long necks to reach leaves high in trees, especially from acacia trees. They mainly eat plants and can spend many hours feeding each day. Giraffes usually live in groups and communicate using sounds and body movements. They are native to Africa and are commonly found in grasslands and open woodlands.",
    "The dolphin is an intelligent marine mammal that lives in oceans and some rivers. It has a smooth body, a long snout, and a strong tail that helps it swim quickly. Dolphins communicate with one another using clicks, whistles, and other sounds. They are social animals and often travel in groups called pods. Dolphins eat fish, squid, and other small sea animals. They are known for their intelligence, playful behavior, and ability to learn different behaviors."
]

query = "which is marine mammal"

doc_embedding = embeddings.embed_documents(animals_docs)
query_embedding = embeddings.embed_query(query)

similarity_score = cosine_similarity([query_embedding], doc_embedding)[0]

print(similarity_score)
print("------------------------------------------------")
index, score = sorted(list(enumerate(similarity_score)), key=lambda x:x[1])[-1]

print(query)
print(animals_docs[index])
print("score", score)


