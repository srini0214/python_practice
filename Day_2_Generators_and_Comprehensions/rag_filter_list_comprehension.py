results = [{"doc_id": 1, "score": 0.9}, {"doc_id": 2, "score": 0.7}]

#Write a single-line list comprehension to get only the doc_id of results where the score > 0.85.

filtered_results = [result["doc_id"] for result in results if result["score"] > 0.85]

print(filtered_results)