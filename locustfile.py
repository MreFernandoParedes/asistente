import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {
                        "content": random.choice(
                            [
                                "¿Cuál es el costo y requisitos para obtener DNI por primera vez?",
                                "¿Cuál es el costo y requisitos para solicitar la expedición de un pasaporte electrónico?",
                                "¿Requiero de asistencia consular, qué debo hacer?",
                                "¿Cómo apostillar un documento?",
                            ]
                        ),
                        "role": "user",
                    },
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {"content": "¿Requiero de asistencia consular, qué debo hacer?", "role": "user"},
                    {
                        "content": "Debes acercarte a una ofician consular.",
                    },
                    {"content": "¿Cual es el costo del derecho consular por exhorto?", "role": "user"},
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )


class ChatVisionUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat/stream",
            json={
                "messages": [
                    {
                        "content": "Can you identify any correlation between oil prices and stock market trends?",
                        "role": "user",
                    }
                ],
                "context": {
                    "overrides": {
                        "top": 3,
                        "temperature": 0.3,
                        "minimum_reranker_score": 0,
                        "minimum_search_score": 0,
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "suggest_followup_questions": False,
                        "use_oid_security_filter": False,
                        "use_groups_security_filter": False,
                        "vector_fields": ["embedding", "imageEmbedding"],
                        "use_gpt4v": True,
                        "gpt4v_input": "textAndImages",
                    }
                },
                "session_state": None,
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat/stream",
            json={
                "messages": [
                    {"content": "Compare the impact of interest rates and GDP in financial markets.", "role": "user"}
                ],
                "context": {
                    "overrides": {
                        "top": 3,
                        "temperature": 0.3,
                        "minimum_reranker_score": 0,
                        "minimum_search_score": 0,
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "suggest_followup_questions": False,
                        "use_oid_security_filter": False,
                        "use_groups_security_filter": False,
                        "vector_fields": ["embedding", "imageEmbedding"],
                        "use_gpt4v": True,
                        "gpt4v_input": "textAndImages",
                    }
                },
                "session_state": None,
            },
        )
