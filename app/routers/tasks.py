from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import Task, TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _get_task_or_404(task_id: int, session: Session) -> Task:
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate, session: Session = Depends(get_session)) -> Task:
    task = Task.model_validate(task_in)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.get("", response_model=list[TaskRead])
def list_tasks(session: Session = Depends(get_session)) -> list[Task]:
    statement = select(Task).order_by(Task.criada_em.desc())
    return list(session.exec(statement).all())


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session)) -> Task:
    return _get_task_or_404(task_id, session)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: int,
    task_in: TaskUpdate,
    session: Session = Depends(get_session),
) -> Task:
    task = _get_task_or_404(task_id, session)
    update_data = task_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)) -> Response:
    task = _get_task_or_404(task_id, session)
    session.delete(task)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
