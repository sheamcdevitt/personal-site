import graphene
from ..types import ArticleType
from ..models import Article

class ArticleInput(graphene.InputObjectType):
  id = graphene.ID()
  title = graphene.String()
  description = graphene.String()
  created_at = graphene.DateTime()
  

class CreateArticle(graphene.Mutation):
  class Arguments:
    input = ArticleInput(required=True)

  article = graphene.Field(ArticleType)

  @staticmethod
  def mutate(root, info, input=None):
    article = Article(
      title=input.title,
      description=input.description,
      created_at=input.created_at
    )
    article.save()
    return CreateArticle(article=article)

class Mutation(graphene.ObjectType):
  create_article = CreateArticle.Field()