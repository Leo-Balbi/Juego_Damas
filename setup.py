from setuptools import setup, find_packages

setup(
    name="juego_damas",
    version="1.0.0",
    description="Juego de Damas clásico implementado en Python con Pygame",
    author="Leonardo Balbi",
    author_email="leonardobalbi22112@gmail.com",
    packages=find_packages(),  # Busca automáticamente paquetes en el proyecto
    install_requires=[
        "pygame>=2.6.1"
    ],
    entry_points={
        'console_scripts': [
            'juego_damas = main:main',  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
