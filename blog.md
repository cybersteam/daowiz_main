---
layout: page
title: My Blog
permalink: /blog/
---

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }} - {{post.date | date_to_string}}</a>
    </li>
  {% endfor %}
</ul>
