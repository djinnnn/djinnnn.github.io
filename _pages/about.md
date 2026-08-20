---
permalink: /
title: "Home"
description: "Yue Wu is a Ph.D. candidate at Tsinghua University researching system and network security."
redirect_from: 
  - /about/
  - /about.html
---

## About Me {#about}

I am a Ph.D. candidate in the Institute of Network Science and Cyberspace at Tsinghua University, advised by [Prof. Jiahai Yang](https://nmgroup.tsinghua.edu.cn/yjh/). Before that I received my B.E. degree in Software Engineering (Cyber Security) from the University of Electronic Science and Technology of China (UESTC).

My research interests lie in System and Network Security, specifically in automated vulnerability discovery and large-scale security measurement. I am also actively pursuing research in LLM4Sec.

Please feel free to contact me if you are interested in relevant research or would like to discuss potential collaborations!

## Research Interests

- **System and Network Security** — automated vulnerability discovery and large-scale security measurement
- **LLM4Sec** — applying large language models to security analysis and automation

## Publications {#publications}

{% if site.data.publications and site.data.publications.size > 0 %}
<div class="publications">
{% for p in site.data.publications %}
  <article class="publication-item">
    <div class="publication-year">{{ p.year }}</div>
    <div class="publication-body">
      <h3 class="publication-title">
        {% if p.url %}
          <a href="{{ p.url }}"{% if p.url contains '://' %} rel="noopener"{% endif %}>{{ p.title }}</a>
        {% else %}
          {{ p.title }}
        {% endif %}
      </h3>
      <p class="publication-authors">
        {% assign authors_parts = p.authors | split: ' and ' %}
        {% for author in authors_parts %}
          {% assign clean_author = author | strip %}
          {% if clean_author == 'Y Wu' or clean_author == 'WU Yue' or clean_author == 'Yue Wu' %}<strong>{{ clean_author }}</strong>{% else %}{{ clean_author }}{% endif %}{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </p>
      <p class="publication-venue">{{ p.venue }}{% if p.year %}, {{ p.year }}{% endif %}</p>
      {% if p.url %}<a class="publication-link" href="{{ p.url }}"{% if p.url contains '://' %} rel="noopener"{% endif %}>Paper details <span aria-hidden="true">→</span></a>{% endif %}
    </div>
  </article>
{% endfor %}
</div>
{% else %}
<p>Publication information will be added soon.</p>
{% endif %}

## Contact

Email: [{{ site.author.email }}](mailto:{{ site.author.email }})
