---
layout: page
title: My Blog
permalink: /blog/
---

<ul>
  {% for post in site.categories.blog1 %}
    <li>
      <a href="{{ post.url }}">- {{post.date | date_to_string}} - {{ post.title }}</a><br>
    </li>
  {% endfor %}
</ul>
