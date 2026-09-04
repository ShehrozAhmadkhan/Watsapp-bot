An over view of what i learned today.

The rag pipeline i built is a single turn conversational based. If i will ask question it will embed the question , query the database to find relevant chunks, and then pass it to llm to generate a answer. But their is an issue.

for example:
user: what is class attendence policy?
assistant: It is 75%.
user: what if it is low?

Now single turn conversational bot will be problematic because the question is incomplete, and if it will find the chunks those will not be relevant.

solution: Multi turn conversation, Conversational memory, Query Reformulation

When we give an llm context of previous conversation/history this is known as conversational memory.

what we do is we create a stand-alone query by using previous context and new question through llm. Then we embed the question and find relevant chunks, and then we pass these relevant chunks, history and new question to llm to generate an answer and this step continue for the rest of the convo.