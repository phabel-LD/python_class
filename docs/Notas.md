#Git & GitHub

##Git

Al desarrollar software, se busca:

* Resolver algún problema
* Que el codigo sea usado por alguien más.
* Software sea fácil de entender por alguien más.
* Sea fáciomente modificable.
* Colaborar con alguien más.

Es decir, siguiendo la **filosofía del software libre**. Por lo que es menester que el código esté propiamente documentado.

Para lograrlo se necesita...

* _Usar estándares de codificación_: reglas para codificar y métodos. Para _python_ es _PEP8_. La guía  de estilo de Google: [https://google.github.io/styleguide]()

* _Notaciones o estándares de nombrado_: indica cómo nombrar variables.
* _Buenas prácticas_: encabezados de progrs, documentación interna, nombre significativo de variable y métodos/funciones, nombre significativo de progrs, organización de código (directories, files)[directory structure], compartir para retroalimentación.
* _Control de versiones del código_: Incluir la versión en la documentación. Y seguir cambios de versiones. Para ello, se usa Git.

### ¿Cómo controlar código?

#### Forma Manual

Versionamiento está constituido por dos dígitos, versiones primarias y secundarias (X,Y).

##### Reglas:
* _X (major)_: Cuando el programa liberado es "estable". La versión principal se cambia
* _Y (minor)_: Cambios mínimos, no sustituyen _de novo_ a la versión major.

#### GIT: versionador automático

Herramienta para llevar seguimiento de cmabios en archivos _.txt_. No funciona eficientmente en archivos binarios (Word, .jpng, ...).
Permite decidir cuáles cambios se harán.

##### Controlar código
* Es como tener un "do/undo" ilimitado.
* Permite que muchas personas trabajen paralelamente.
* GIT es un sistema de control de versiones para rastrear los cambios de nuestro código durante el desarrollo del web. Es muy popular, por lo que hay mucho soporte.

##### Git de manera local

El acceso y calteración al código es _personal_.

Se proporciona un mail para version de Git.

```
phabel:~ phabellopez$ git --version
git version 2.30.1
phabel:~ phabellopez$ git config --global user.email "phabelphabel:~ phabellopez$ git config --global user.email "phabel2001@gmail.com"
phabel:~ phabellopez$ git config --list
credential.helper=osxkeychain
user.name=phabel
user.email=phabel2001@gmail.com

```

##### Git + GitHub

Abre el panorama porque el código está en el _web para consulta y uso_; creando comunidades de desarrollo, perimitiendo la retroalimentación activa. Un _ambiente colaborativo_.

Una rama de Git es un apuntador que permite hacer referencia a cada uno de los commmits. Rama por default de Git es la *rama master*, la cual se crea por defecto al usar el comando *git init*. Las ramas se pueden asociar a módulos, que después se pueden cargar a la Rama master; es decir, el edo. final.

Para controlar más de un archivo






#### Commands

*git status*: indica el edo. de los archivos controlados por Git.

*git config --list*

*git --version*

*git config --[global user.name]*

*git config --[global user.email]*

*git add* :(temporal en area de preparación). Se reusa con cada modificación significativa (versión) para pasar los cambios al area de preparación.

*git commit -m "Mensaje"* : Consolida los cambios. Manda al repositorio con el seguimiento de los cambios para hacerlo permanente. *-m* para mensaje corto <50 caracteres, y  '*-a'  para mensajes más largos*; pero lo mejor es siempre usar mensajes cortos (<70 caracteres) sobre los cambios realizados; separando e mensajeen un title y un body. Se puede mover un repositorio Git mientras el directorio *.git* no se vea afectado.
Se puede modificar el mensaje del *commit* mas reciente con: *git commit --amend -m "Message"*

*mkdir*

*git init* : Inicializa un repositorio con git. Crea carpeta *(.git/)* oculta en el directorio donde se trabaja con Git. Trabaja sobre todas las subcarpetas dentro de la carpeta donde se inicializó. No es buena idea anidar carpetas con git subordiandas a otras carpetas con git. Es decir, *git controla todo los repositorios subordinado al repositorio raiz de git*

*git log* despliega el historia de *commmits*

*git log --oneline*

*git log -N*

