import graphene
from .types import ArticleType
from .models import Article
from .mutations.Article import Mutation as ArticleMutation


class Query(graphene.ObjectType):
  article = graphene.Field(ArticleType, id=graphene.Int())
  articles = graphene.List(ArticleType)

  def resolve_article(self, info, **kwargs):
    return Article.objects.first()

  def resolve_articles(self, info, **kwargs):
    return Article.objects.all()

class Mutation(ArticleMutation,object):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)

