# LAB04_S04_DAE

# 🌟 Guía Práctica: Relaciones entre Modelos en Django

Este proyecto es una guía práctica para entender y aplicar las relaciones entre modelos en Django 🧩. A través de una app de gestión de biblioteca, aprenderás a usar ForeignKey, OneToOneField y ManyToManyField de forma clara y funcional.

---

## 📚 ¿Qué construimos?

Creamos una app de biblioteca con las siguientes entidades:

- 👨‍🎨 **Autores** – Personas que escriben libros  
- 📚 **Libros** – Obras publicadas  
- 🏷️ **Categorías** – Géneros literarios  
- 👤 **Perfiles** – Info adicional de los autores  
- 🏢 **Editoriales** – Empresas que publican libros  

---

## 🔄 Relaciones implementadas

- **Uno a Muchos** (1️⃣➡️🔢): Un autor puede tener varios libros  
- **Uno a Uno** (1️⃣➡️1️⃣): Cada autor tiene un perfil único  
- **Muchos a Muchos** (🔢↔️🔢): Libros pueden estar en varias categorías  
- **Muchos a Muchos con datos extra** (🔗): Publicaciones con info adicional por país/editorial  
