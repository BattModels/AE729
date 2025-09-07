# Electrochemical Energy Storage Systems

This site contains the code examples used in the AEROSP 729-004 / MATSCIE 593-001 / MECHENG 699-001 course taught at the University of Michigan by [Prof. Venkat Viswanathan](https://eeg.engin.umich.edu/).

## Time and Location

Monday - Wednesday, 9:00 - 10:30 AM, FXB 1024
## About the course

The electrification of mobility (automotive and aviation) requires large-scale electrochemical energy storage systems.  Batteries play a prominent role in sustainable transportation, aviation, and portable electronics.  This course introduces the principles and mathematical models of electrochemical energy storage with a specific focus on Li-ion batteries. Students will study thermodynamics and reaction kinetics pertaining to electrochemical reactions, and phase transformations relating to batteries. This course will ensure a detailed understanding of the porous electrode modeling of Li-ion batteries and how they can be used in systems (modules, packs) for electric mobility.

## Schedule
<style>
/* Base table */
table.schedule-mtwf {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}
table.schedule-mtwf, table.schedule-mtwf th, table.schedule-mtwf td {
  border: 1px solid #ccc;
}
table.schedule-mtwf th, table.schedule-mtwf td {
  padding: 8px;
  text-align: left;
  vertical-align: top;
}

/* Header & striping – LIGHT (theme toggle) */
html[data-theme="light"] table.schedule-mtwf thead tr,
body[data-theme="light"] table.schedule-mtwf thead tr {
  background: #f2f2f2;  /* extremely light gray */
  color: #000;
}
html[data-theme="light"] table.schedule-mtwf tbody tr:nth-child(even),
body[data-theme="light"] table.schedule-mtwf tbody tr:nth-child(even) {
  background: #fafafa;
}

/* Header & striping – DARK (theme toggle) */
html[data-theme="dark"] table.schedule-mtwf thead tr,
body[data-theme="dark"] table.schedule-mtwf thead tr {
  background: #444;
  color: #fff;
}
html[data-theme="dark"] table.schedule-mtwf tbody tr:nth-child(even),
body[data-theme="dark"] table.schedule-mtwf tbody tr:nth-child(even) {
  background: #2a2a2a;
}

/* Colored cells for events */
.cell-class    { font-weight: 500; }
.cell-holiday  { font-weight: 600; }
.cell-exam     { font-weight: 600; }

/* Light colors */
html[data-theme="light"] .cell-class   { background: #eaf7ea !important; }   /* green tint */
html[data-theme="light"] .cell-holiday { background: #ffe9e9 !important; }   /* red tint  */
html[data-theme="light"] .cell-exam    { background: #e8f4ff !important; }   /* cyan tint */

/* Dark colors (subtle translucency) */
html[data-theme="dark"] .cell-class   { background: rgba(76, 175, 80, 0.30) !important; color: #fff; }
html[data-theme="dark"] .cell-holiday { background: rgba(244, 67, 54, 0.30) !important;  color: #fff; }
html[data-theme="dark"] .cell-exam    { background: rgba(3, 169, 244, 0.30) !important;  color: #fff; }

/* Fallback if the theme attribute isn't present (use OS pref) */
@media (prefers-color-scheme: dark) {
  table.schedule-mtwf thead tr { background: #444; color: #fff; }
  table.schedule-mtwf tbody tr:nth-child(even) { background: #2a2a2a; }
}
</style>

````{div} full-width
<table class="schedule-mtwf">
  <thead>
    <tr>
      <th>Week (Mon)</th>
      <th>M</th>
      <th>T</th>
      <th>W</th>
      <th>Th</th>
      <th>F</th>
      <th>Topics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Aug 25, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>Introduction <br> 1.1 Basics of Electrochemical Devices</td>
    </tr>
    <tr>
      <td>Sep 1, 2025</td>
      <td class="cell-holiday">Labor Day</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>1.2 Energy Storage</td>
    </tr>
    <tr>
      <td>Sep 8, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td>HW1 due</td>
      <td>1.3 Equivalent Circuit Models<br>2.1 Thermodynamics - Phase transformation</td>
    </tr>
    <tr>
      <td>Sep 15, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>2.2 Entropy <br> 2.3 Intercalation Cathodes (LFP)</td>
    </tr>
    <tr>
      <td>Sep 22, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td> HW2 due</td>
      <td>2.4 Insertion Anodes (Graphite)<br>3.1 Electrode Kinetics (Butler-Volmer)</td>
    </tr>
    <tr>
      <td>Sep 29, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>3.2 Electrode Kinetics (Marcus)<br>3.3 Electrode Kinetics (Advanced Models)</td>
    </tr>
    <tr>
      <td>Oct 6, 2025</td>
      <td class="cell-class">Class, HW3 due</td>
      <td></td>
      <td class="cell-exam">Midterm</td>
      <td class="cell-exam">Midterm</td>
      <td></td>
      <td>Review for midterm</td>
    </tr>
    <tr>
      <td>Oct 13, 2025</td>
      <td class="cell-holiday">Fall Break</td>
      <td class="cell-holiday">Fall Break</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>4.1 Electrode-Electrolyte Interfaces</td>
    </tr>
    <tr>
      <td>Oct 20, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>4.2 Electrode-Electrolyte Interfaces<br>4.3 Polymer Electrolytes and Ionic Liquids</td>
    </tr>
    <tr>
      <td>Oct 27, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td>HW4 due</td>
      <td>5.1 Transport in Solids <br> 5.2 Transport in Liquids</td>
    </tr>
    <tr>
      <td>Nov 3, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>5.3 Porous media <br> 6.1 Porous Electrode Theory</td>
    </tr>
    <tr>
      <td>Nov 10, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>6.2 Modified Porous Electrode Theory<br>7.1 Battery Cell Modeling</td>
    </tr>
    <tr>
      <td>Nov 17, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class</td>
      <td></td>
      <td></td>
      <td>7.2 Battery pack Modeling, PyBaMM (demo)</td>
    </tr>
    <tr>
      <td>Nov 24, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-holiday">Thanksgiving</td>
      <td class="cell-holiday">Thanksgiving</td>
      <td class="cell-holiday">Thanksgiving</td>
      <td></td>
    </tr>
    <tr>
      <td>Dec 1, 2025</td>
      <td class="cell-class">Class</td>
      <td></td>
      <td class="cell-class">Class, Project due</td>
      <td></td>
      <td></td>
      <td>Finals Review</td>
    </tr>
    <tr>
      <td>Dec 8, 2025</td>
      <td class="cell-exam">Final</td>
      <td class="cell-exam">Final</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
````

<!-- ```{tableofcontents} -->
<!-- ``` -->
