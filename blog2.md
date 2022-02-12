---
layout: page
title: My Blog2
permalink: /blog2/
---

Oh hello!

<ul>
  {% for post in site.categories.blog2 %}
    <li>
      <a href="{{ post.url }}">- {{post.date | date_to_string}} - {{ post.title }}</a><br>
    </li>
  {% endfor %}
</ul>
