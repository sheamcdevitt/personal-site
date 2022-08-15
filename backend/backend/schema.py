import graphene
from frontend.schema import Query as FrontendQuery 
from frontend.schema import Mutation as FrontendMutation


class Query(FrontendQuery, graphene.ObjectType):
    pass

class Mutation(FrontendMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation),