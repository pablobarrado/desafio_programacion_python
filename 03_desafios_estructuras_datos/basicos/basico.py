#  Users/pablobarradogarcia/Library/Python/3.9/bin/virtualenv env  
#  source env/source/active/bin/activate
#  Virtualenv es uno de los paquetes que puede ser usado para crear ambientes virtuales en Python.
#  Es bastante estable y compatible con una gran cantidad de librerías, es fácil de instalar y de usar. 
# Para instalar Virtualenv, nos vamos a la terminal y lo instalamos con pip, con la instrucción «pip install virtualenv». 
# Una vez finalizada la instalación, podemos crear nuestro primer ambiente. 
# Los ambientes con Virtualenv se crean dentro de la carpeta donde estamos ubicados, por ello es preferible que para 
# cada proyecto se tenga un ambiente propio. Creamos nuestro ambiente con la instrucción «virtualenv» junto al nombre 
# del ambiente, en este caso le pondré «env». En la carpeta donde hemos creado el ambiente,
#  podemos ver que se creó una carpeta con el mismo nombre de nuestro ambiente; esta es la carpeta del ambiente 
# que contiene toda la información que nos permitirá instalar los paquetes que necesitamos en nuestro proyecto. 
# Para activar el ambiente escribimos en Windows «env\Scripts\activate». Veremos que el ambiente está activo cuando 
# nos sale antes de la línea, entre paréntesis, el nombre del ambiente que creamos.
# 
#  La instrucción para Mac o Linux es «source env\bin\activate». 
# Podemos desactivar el ambiente usando «deactivate». 
# Como vemos, ya no nos aparece entre paréntesis el nombre del ambiente, lo que indica que ya no estamos dentro de él.
#  Funciona igual para Mac o Linux. Finalmente, podemos borrar nuestro ambiente en caso de que ya no lo queramos usar o 
# ya no lo necesitemos. Esto lo hacemos en Windows con la instrucción «rmdir env /s». 
# Le damos que sí queremos finalizar el ambiente, y veremos que el ambiente ya no existe en nuestra carpeta. 
# La instrucción para Mac o Linux es «rm -f env»
