{% args files %}
{% include "header.tpl" %}
<div class="maindiv">
<h2>Log Files</h2>
<div id="logTable">
    <table>
        {% for file in files %}
        <tr>
            <td><a href='/logs/{{ file }}' target="_blank">{{ file }}</a></td>
        </tr>
        {% endfor %}
    </table>
</div>
</div>
{% include "footer.tpl" %}
