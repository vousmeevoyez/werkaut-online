# werkaut.online
<img src="https://raw.githubusercontent.com/vousmeevoyez/werkaut-online/master/wger/core/static/images/logos/logo.png" width="100" height="100" />

werkaut.online is web application that helps
you manage your personal workouts, weight and diet plans and can also be used
as a simple gym management utility. It offers a REST API as well, for easy
integration with other projects and tools.

![Workout plan](https://raw.githubusercontent.com/vousmeevoyez/werkaut-line/master/wger/software/static/images/workout.png)


### Development version

We provide a docker file that sets everything up for development (however this won't
persist any data)

````shell script
docker run -ti  \
    -v /path/to/your/wger/checkout:/home/wger/src \
    --name werkaut.online \
    --publish 8000:8000 \ 
    wger/server
````

Then just open <http://localhost:8000> and log in as: **admin**, password **adminadmin**

For more info, check the [README in wger/extras/developemt](
 ./extras/docker/development/README.md
).

Alternatively you can use the production compose file for development as well,
just bind your local source code into the web container (see the docker-compose.yml
file for details). You will also probably want to set `DJANGO_DEBUG to false

## License

The application is licensed under the Affero GNU General Public License 3 or
later (AGPL 3+).

The initial exercise and ingredient data is licensed additionally under one of
the Creative Commons licenses, see the individual exercises for more details.

The documentation is released under a CC-BY-SA: either version 4 of the License,
or (at your option) any later version.

Some images were taken from Wikipedia, see the SOURCES file in their respective
folders for more details.
