---
permalink: /
title: "Home"
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# Yue Wu (吴越)
I am a Ph.D. student in the Institute of Network Science and Cyberspace at Tsinghua University, advised by [Prof. Jiahai Yang](https://nmgroup.tsinghua.edu.cn/yjh/).  Before that I received my B.E. degree in Software Engineering (Cyber Security) from the University of Electronic Science and Technology of China (UESTC).

My research interests lie in System and Network Security, specifically in automated vulnerability discovery and large-scale security measurement. I am also actively pursuing research in LLM4Sec.

Please feel free to contact me if you are interested in relevant research or would like to discuss potential collaborations!

---

# Publications

{% if site.data.publications and site.data.publications.size > 0 %}
<div class="publications">
{% for p in site.data.publications %}
  <div class="publication-item">
    <div class="publication-header">
      <div class="publication-title">{{ p.title }}</div>
      <div class="publication-meta-tag">
        {% if p.venue %}{{ p.venue }}{% endif %}
        {% if p.year %}<span class="publication-year">{{ p.year }}</span>{% endif %}
      </div>
    </div>
    <div class="publication-authors">
      {% assign authors_parts = p.authors | split: ' and ' %}
      {% for author in authors_parts %}
        {% if author contains 'Wu' %}
          <strong>{{ author | strip }}</strong>{% if forloop.last %}{% else %}, {% endif %}
        {% else %}
          {{ author | strip }}{% if forloop.last %}{% else %}, {% endif %}
        {% endif %}
      {% endfor %}
      {% if p.url %}<a href="{{ p.url }}" class="publication-link">Link</a>{% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% else %}
Please add a `publications.bib` and run the conversion script to populate publications, or add entries to `_data/publications.yml`.
{% endif %}

---

# Education

- 2015–2019 — B.S., Major, Institution
- 2019–2022 — Ph.D., Major, Institution

请替换为你的实际学历条目。

---

# Selected Honors and Awards

- 2021 — Award Name, Issuer, 简短说明
- 2019 — Another Award, Issuer

列出你希望展示的若干重要奖项。

---

如果你希望我用中文或英文排版、自动导入 Google Scholar / ORCID / BibTeX，告诉我具体偏好，我可以继续完善。 