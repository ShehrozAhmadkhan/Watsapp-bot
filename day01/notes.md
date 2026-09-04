RAG Pipeline Revision

Apni existing PDF-chat pipeline revise ki:
1. Data loading (GPT-generated, PDF, text files)
2. Word-based chunking with overlap
3. Batch-based embedding (OpenAI text-embedding-small)
4. Batch upsert into Pinecone
5. Query embedding + similarity search
6. LLM (GPT-4o mini) answer generation

Gap identify kiya: conversation memory/multi-turn handling abhi tak
nahi kiya — Uni-Assist mein naya seekhna hoga.