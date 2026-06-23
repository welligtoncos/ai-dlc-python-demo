from datetime import datetime, timezone

from sqlmodel import Session

from app.models import Task


def test_sc01_create_task_returns_201(client):
    response = client.post(
        "/tasks",
        json={"titulo": "Minha tarefa", "descricao": "Detalhes"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["titulo"] == "Minha tarefa"
    assert data["descricao"] == "Detalhes"
    assert data["concluida"] is False
    assert data["criada_em"].endswith("Z")


def test_sc02_create_without_titulo_returns_422(client):
    response = client.post("/tasks", json={"descricao": "sem titulo"})
    assert response.status_code == 422


def test_sc03_create_with_blank_titulo_returns_422(client):
    response = client.post("/tasks", json={"titulo": "   "})
    assert response.status_code == 422


def test_sc04_list_tasks_ordered_by_criada_em_desc(client, session: Session):
    older = Task(
        titulo="Antiga",
        criada_em=datetime(2026, 1, 1, tzinfo=timezone.utc),
    )
    newer = Task(
        titulo="Nova",
        criada_em=datetime(2026, 6, 1, tzinfo=timezone.utc),
    )
    session.add(older)
    session.add(newer)
    session.commit()

    response = client.get("/tasks")
    assert response.status_code == 200
    titles = [item["titulo"] for item in response.json()]
    assert titles == ["Nova", "Antiga"]


def test_sc05_get_nonexistent_task_returns_404(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_sc06_partial_update_preserves_other_fields(client):
    create_response = client.post(
        "/tasks",
        json={"titulo": "Original", "descricao": "Manter"},
    )
    task_id = create_response.json()["id"]

    response = client.put(f"/tasks/{task_id}", json={"concluida": True})
    assert response.status_code == 200
    data = response.json()
    assert data["concluida"] is True
    assert data["titulo"] == "Original"
    assert data["descricao"] == "Manter"


def test_sc07_put_with_empty_titulo_returns_422(client):
    create_response = client.post("/tasks", json={"titulo": "Valida"})
    task_id = create_response.json()["id"]

    response = client.put(f"/tasks/{task_id}", json={"titulo": ""})
    assert response.status_code == 422


def test_sc08_delete_existing_task_returns_204(client):
    create_response = client.post("/tasks", json={"titulo": "Remover"})
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    assert response.content == b""

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_sc09_delete_nonexistent_task_returns_404(client):
    response = client.delete("/tasks/999")
    assert response.status_code == 404


def test_create_strips_titulo_whitespace(client):
    response = client.post("/tasks", json={"titulo": "  Espaços  "})
    assert response.status_code == 201
    assert response.json()["titulo"] == "Espaços"


def test_get_existing_task_returns_200(client):
    create_response = client.post("/tasks", json={"titulo": "Buscar"})
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Buscar"
