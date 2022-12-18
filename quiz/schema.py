import graphene
from graphene_django import DjangoObjectType,DjangoListField
from .models import *

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields=('id','name')


class QuizzesType(DjangoObjectType):
    class Meta:
        model=Quizzes
        fileds=('title','category','date_created')


class QuestionType(DjangoObjectType):
    class Meta:
        model=Question
        fileds=('quiz','title','difficulty')


class AnswerType(DjangoObjectType):
    class Meta:
        model=Answer
        fileds=('question','answer_text','is_right')


class Query(graphene.ObjectType):
    all_categories=graphene.List(CategoryType)
    all_answers=graphene.List(AnswerType)
    all_questions=graphene.List(QuestionType)
    all_quizzes=DjangoListField(QuizzesType)

    spec_quiz=graphene.Field(QuizzesType,id=graphene.ID(required=True))

    def resolve_all_categories(self,info):
        return Category.objects.all()

    def resolve_all_answers(self,info):
        return Answer.objects.all()

    def resolve_spec_quiz(self,info,id):
        return Quizzes.objects.get(pk=id)

class CreateCategory(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
    
    category=graphene.Field(CategoryType)
    @classmethod
    def mutate(cls,self,info,name):
        category=Category.objects.create(name=name)
        category.save()
        return CreateCategory(category=category)

class update_category(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
        name=graphene.String()
    category=graphene.Field(CategoryType)

    @classmethod
    def mutate(cls,self,info,id,name):
        category=Category.objects.get(id=id)
        category.name=name
        category.save()
        return update_category(category=category)

class delete_category(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
    category=graphene.Field(CategoryType)
    @classmethod
    def mutate(cls,self,info,id):
        category=Category.objects.get(id=id)
        category.delete()
        return delete_category(category=category)


# class create_category(graphene.Mutation):
#     class Arguments:
#         name=graphene.String()

#     category=graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls,root,info,name):
#         category=Category.objects.create(name=name)
#         category.save()
#         return create_category(category=category)

class Mutation(graphene.ObjectType):
    CreateCategory=CreateCategory.Field()
    DeleteCategory=delete_category.Field()
    update_Category=update_category.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)


# import graphene
# from graphene_django import DjangoObjectType,DjangoListField
# from .models import Quizzes,Category,Question,Answer

# class CategoryType(DjangoObjectType):
#     class Meta:
#         model=Category
#         fields=("id","name")

# class QuizzesType(DjangoObjectType):
#     class Meta:
#         model=Quizzes
#         fields=("id","title",'category')

# class QuestionType(DjangoObjectType):
#     class Meta:
#         model=Question
#         fields=("title",'quiz')

# class AnswerType(DjangoObjectType):
#     class Meta:
#         model=Answer
#         fields=("id","question","answer_text")

# class Query(graphene.ObjectType):

#     #using DjangoListField we no need to write an return 
#     # to return objects and no need to write resolve
#     #functions also

#     all_quizzes=graphene.List(QuizzesType)

#     all_questions=graphene.List(QuestionType)
#     # all_answers=graphene.Field(AnswerType,id=graphene.Int())
#     all_answers=graphene.List(AnswerType)
#     all_categories=graphene.List(CategoryType)
#     # all_quizzes=graphene.List(QuizzesType)
#     # all_questions=graphene.List(QuestionType)
#     def resolve_all_categories(root,info):
#         return Category.objects.all()

#     def resolve_all_quizzes(root,info):
#         return Quizzes.objects.all()


#     # def resolve_all_questions(root,info,id):
#     #     return Question.objects.get(pk=id)

#     def resolve_all_questions(root,info):
#         return Question.objects.all()

#     def resolve_all_answers(root,info):
#         # retur n Answer.objects.filter(question=id).all()
#         return Answer.objects.all()
#     # def resolve_all_questions(root,info):
#     #     return Question.objects.all()

# class Update_category(graphene.Mutation):
#     class Arguments:
#         name=graphene.String(required=True)
#         id=graphene.ID(required=True)

#     category=graphene.Field(CategoryType)


#     @classmethod
#     def mutate(cls,root,info,name,id): 
#         category=Category.objects.get(id=id)
#         category.name=name
#         category.save()
#         return Update_category(category=category)

# class delete_category(graphene.Mutation):
#     class Arguments:
#         id=graphene.ID(required=True)

#     category=graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls,root,info,id):
#         category=Category.objects.get(id=id)
#         category.delete()
#         category.save()
#         return delete_category(category=category)

# class update_answer(graphene.Mutation):
#     class Arguments:
#         id=graphene.ID()
#         answer_text=graphene.String()

#     answer=graphene.Field(AnswerType)

#     @classmethod
#     def mutate(cls,root,info,id,answer_text):
#         answer=Answer.objects.get(id=id)
#         answer.answer_text=answer_text
#         answer.save()
#         return update_answer(answer=answer)


# class QuizMutation(graphene.Mutation):
#     class Arguments:
#         title=graphene.String(required=True)
#         # Category=graphene.String(required=True)
#     quiz=graphene.Field(QuizzesType)

#     @classmethod
#     def mutate(cls,root,info,title):
#         quiz=Quizzes(title=title)
#         quiz.save()
#         return QuizMutation(quiz=quiz)



# class delete_question(graphene.Mutation):
#     class Arguments:
#         id=graphene.ID()
#     question=graphene.Field(QuestionType)

#     @classmethod
#     def mutate(cls,root,info,id):
#         question=Question.objects.get(pk=id)
#         question.delete()
#         return delete_question(question=question)



# class Mutation(graphene.ObjectType):
#     delete_category=delete_category.Field()
#     update_answer=update_answer.Field()
#     update_category=Update_category.Field()
#     update_quiz=QuizMutation.Field()
#     create_category=create_category.Field()
#     delete_question=delete_question.Field()
   

# schema=graphene.Schema(query=Query,mutation=Mutation)
