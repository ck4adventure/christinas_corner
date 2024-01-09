.PHONY: reset clean makemigrations migrate createsuperuser run shell

reset: clean makemigrations migrate createsuperuser

clean:
		rm app/db.sqlite3
		find ./app/recipes -type f -name 000\* -exec rm {} \;

makemigrations:
		python app/manage.py makemigrations

migrate:
		python app/manage.py migrate

createsuperuser:
		python app/manage.py createsuperuser

run:
		python app/manage.py runserver

shell:
		python app/manage.py shell