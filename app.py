from flask import Flask, render_template, redirect, url_for, request
from typing import List
from sqlalchemy.sql.functions import user
from models import db, Article, User
from flask_migrate import Migrate
from markupsafe import escape
from forms import ArticleForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db?check_same_thread=False'
db.app = app
db.init_app(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = 'you-will-never-guess'
Bootstrap(app)


@app.route('/')
def homepage():
    articles: List[Article] = Article.query.all()
    return render_template('articles_main.html', articles=articles)


@app.route('/add', methods=["Get", "Post"])
def add_article():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        image = form.image.data
        href = form.href.data
        article = Article(title=title, body=body, image=image, href=href, user=User.query.first())
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("homepage", article_id=article.id))
    return render_template('add_article.html', form=form)

@app.route('/add78', methods=["Get", "Post"])
def add_article89():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        image = form.image.data
        href = form.href.data
        article = Article(title=title, body=body, image=image, href=href, user=User.query.first())
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("hello_world1", article_id=article.id))
    return render_template('edit.html', form=form)

@app.route('/articles/search')
def search_article():
    q = request.args.get("q", "")
    articles: List[Article] = Article.query.filter(Article.title.like(f"%{q}%") | Article.body.like(f"%{q}%")).all()
    return render_template("articles_main.html", title='Главная страница', articles=articles)

@app.route('/get')
def get_article(article_id):
    articles: Article = Article.query.filter_by(id=article_id).first()
    return render_template('mainpage.html', title="Главная сттраница", articles=articles)


@app.route('/about')
def hello_world1():
    articles: List[Article] = Article.query.all()
    return render_template('legendary car.html', articles=articles)



@app.route('/tech')
def hello_world2():
    return render_template('technologies.html')

@app.route('/articles/<int:article_id>/edit', methods=["GET", "POST"])
def edit_article(article_id):
    article: Article = Article.query.filter_by(id=article_id).first()
    form = ArticleForm()
    if form.validate_on_submit():
        article.title = form.title.data
        article.body = form.body.data
        article.image = form.image.data
        article.href = form.href.data
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("homepage", article_id=article.id))
    else:
        form.title.data = article.title
        form.body.data = article.body
        form.image.data = article.image
        form.href.data = article.href
        return render_template('edit_article.html', form=form)


@app.route('/new')
def hello_world4():
    return render_template('newitems.html')


@app.route('/about/<username>')
def about(username):
    return f'All about {escape(username)}'


if __name__ == '__main__':
    app.run()
