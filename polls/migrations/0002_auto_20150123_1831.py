# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='name_user',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]


# Trecho do SQL gerado pelos migrations

# ^C(django-teste)MAC001085:mysite thiagosoares$ python manage.py sqlmigrate polls 0001
# BEGIN;
# CREATE TABLE "polls_choice" (
#     "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
#     "choice_text" varchar(200) NOT NULL, 
#     "votes" integer NOT NULL);

# CREATE TABLE "polls_question" (
#     "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
#     "question_text" varchar(200) NOT NULL, 
#     "pub_date" datetime NOT NULL);

# CREATE TABLE "polls_choice__new" (
#     "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
#     "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, 
#     "question_id" integer NOT NULL REFERENCES "polls_question" ("id"));


# INSERT INTO "polls_choice__new" (
#     "choice_text", "votes", "id", "question_id") SELECT "choice_text", "votes", "id", 
# NULL FROM "polls_choice";

# DROP TABLE "polls_choice";
# ALTER TABLE "polls_choice__new" RENAME TO "polls_choice";
# CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");

# COMMIT;