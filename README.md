# PyOSX-Info v0.2
A Python script used to gather information about an OS X system.
<br>
<img src='http://i.imgur.com/oaKybcA.png' width='400px'/>
<figcaption>v0.1 Shown</figcaption>

<h3>Requirements</h3>
<ul>
<li>A system running OS X</li>
<li>Python (Tested on 2.7.9)</li>
<li>hurry.filesize (pip install hurry.filesize)</li>
<li>tabulate (pip install tabulate)</li>
<li>Collections/Counter (pip install counter)</li>
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
<li>Boot Session UUID</li>
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
<th>Bluetooth</th>
<td>
<ul>
<li>Version</li>
<li>Paired Device Count</li>
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

<h3>Latest Updates</h3>
New in v0.2:
<ul>
<li>Additions
<ul>
<li>Boot Session UUID</li>
<li>Bluetooth Version</li>
<li>Bluetooth Paired Device Count</li>
</ul>
</li>
<li>Bug Fixes
<ul>
<li>Fixed unit test for swap space bug.  Errored if swap amount changed.</li>
</ul>
</li>
<li>Improvements
<ul>
<li>Added get_system_profiler_data and get_sysctl_data.  Greatly reduces duplicate code.</li>
</ul>
</li>
</ul>