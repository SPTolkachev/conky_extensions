<h1>Conky extensions</h1>
<p>Python scripts that extend the capabilities of conky.</p>


<h2>days_before.py</h2>
<p>Returns the number of days before the specified date (and time).</p>

<h3>Usage</h3>
<pre>days_before.py [options]</pre>

<h3>Options</h3>
<ul>
  <li>
    <h4>-h, --help</h4>
    <p>show this help message and exit</p>
  </li>
  <li>
    <h4>-l LANG, --lang LANG</h4>
    <p>language</p>
  </li>
  <li>
    <h4>-d DAY, --day DAY</h4>
    <p>target day</p>
  </li>
  <li>
    <h4>--hours</h4>
    <p>enable hours output</p>
  </li>
  <li>
    <h4>-m, --minutes</h4>
    <p>enable minutes output</p>
  </li>
  <li>
    <h4>-s, --seconds</h4>
    <p>enable seconds output</p>
  </li>
  <li>
    <h4>-et EVENT_TEXT, --event_text EVENT_TEXT</h4>
    <p>the text that will be displayed after the event</p>
  </li>
</ul>

<h3>Example usage</h3>
<p>File '~/.conky/conkyrc':</p>
<pre>
default_color ffffff
color0 FFA300
color1 DDDDDD

TEXT
${font Noto Sans:size=12}Time before the trip: ${alignr}${font Hack:size=11}${color0}\\
${execp conky_extensions/extensions/days_before.py\\
            --day='2022-06-22 04:00:00'\\
            --event_text="It's time to go :)"\\
}\\
${color}
</pre>
