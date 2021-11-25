from fastapi import APIRouter
from models.student import Student
from config.database import db
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

@student_router.get('/students')
async def find_all_students():
     return listOfStudentEntity(db.students.students.find())

@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
     return studentEntity(db.students.students.find_one({"_id": ObjectId(studentId)}))

@student_router.post('/students')
async def create_student(student:Student):
     db.students.students.insert_one(dict(student))
     return listOfStudentEntity(db.students.students.find())

@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
     db.students.students.find_one_and_update(
          {"_id": ObjectId(studentId)},
          {"$set": dict(student)}
     )
     return studentEntity(db.students.students.find_one({"_id": ObjectId(studentId)}))

@student_router.delete('/students/{studentId}')
async def update_delete(studentId):
     return studentEntity(db.students.students.find_one_and_delete(
          {"_id": ObjectId(studentId)}
     ))
