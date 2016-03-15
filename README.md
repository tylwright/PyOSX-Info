# PyOSX-Info
A Python script used to gather information about an OS X system.
<br>
<img src='http://i.imgur.com/oaKybcA.png' width='400px'/>

<h3>Requirements</h3>
<ul>
<li>A system running OS X</li>
<li>Python (Tested on 2.7.9)</li>
<li>hurry.filesize (pip install hurry.filesize)</li>
<li>tabulate (pip install tabulate)</li>
<li>unittest2 (pip install unittest2)*</li>
</ul>
<i>* only needed if running unit tests</i>

<h3>Running the Script</h3>
```
python pyosx.py <type>
```
For example:
```
python pyosx.py full
python pyosx.py system
```

<h4>Parameters</h4>
<h5>Type</h5>
<table>
<tr>
<th>Parameter Value for Type</th>
<th>Items Shown</th>
</tr>
<tr>
<th>Full</th>
<td>Displays all of the items that are listed below</td>
</tr>
<tr>
<th>System</th>
<td>
<ul>
<li>OS X Version</li>
<li>Hostname</li>
<li>Model</li>
<li>Serial</li>
</ul>
</td>
</tr>
<tr>
<th>UUIDs</th>
<td>
<ul>
<li>Kernel UUID</li>
<li>Hardware UUID</li>
</ul>
</td>
</tr>
<tr>
<th>Clocks</th>
<td>
<ul>
<li>Last Boot</li>
</ul>
</td>
</tr>
<tr>
<th>CPU</th>
<td>
<ul>
<li>Model</li>
<li>Architecture</li>
<li>Total Processors</li>
<li>Physical Cores</li>
<li>Logical Cores</li>
</ul>
</td>
</tr>
<tr>
<th>RAM</th>
<td>
<ul>
<li>Total RAM</li>
<li>Total swap</li>
</ul>
</td>
</tr>
<tr>
<th>Miscellaneous</th>
<td>
<ul>
<li>SMC Version</li>
<li>Boot ROM Version</li>
</ul>
</td>
</tr>
</table>
