

Layouts & Themes
**********************


In-built Demos (Skins)
----------------------

Ubold comes with multiple demos (skins). I.e. ``creative``, ``default``, ``material``, ``modern``, ``purple``, and ``saas``. 
Each of these skins are having respective dark mode available as well. 
You can simply set the context variable demo with the desired value in your template and just include super block to have the desired demo look. E.g.

.. code:: python3
    
        {% block css_wrapper %}
            {% with demo="modern" %}
                {{ block.super }}
            {% endwith%}
        {% endblock css_wrapper%}


-------------------------------------------


Customizing Color Palette
-------------------------
You can even the color palatte of any demo very easily by simply changing the few scss variables value.

In order to modify the colors in existing themes, open the ``_variables.scss`` file from ``static/scss/config/<DEMO_NAME>`` 
and change any variable in it. Your changes would get reflected automatically in any bootstrap based components or elements. 

.. note:: Note that, this requires you to setup and run gulp flow provided in getting started steps.


-------------------------------------------


In-built Layouts
-----------------
Ubold provides multiple choices when it comes to layouting. There are multiple layout choices available. 
I.e. ``Vertical`` (main navigation on "Left"), ``Horizontal`` (main navigation on "Top") and ``Detached`` 
(main navigation on "Left" side but part of main content area). 

.. note:: Check the ``demo`` folder in the templates directory to see the examples.

-------------------------------------------

Customizing Color Mode, Left Sidebar, Topbar, Layout Width and Right Sidebar
-----------------------------------------------------------------------------
Ubold allows you to have customized left sidebar, overall layout width or right sidebar. 
You could turn the left sidebar to different size, theme (look) and size. You can customize it by specifying the 
layout data attribute (``data-layout={}``) on ``body`` element in your html. 
The config object properties accept the following values:


+-----------------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Title                       | Type    | Options                                                                                                                           | Description                                                                                                                                                                                                                                                                                                           |
+=============================+=========+===================================================================================================================================+=======================================================================================================================================================================================================================================================================================================================+
| mode                        | String  | 'light' | 'dark'                                                                                                                  | Changes overall color scheme to light or dark                                                                                                                                                                                                                                                                         |
+-----------------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| width                       | String  | 'fluid' | 'boxed'                                                                                                                 | Changes the width of overall layout to fluid or boxed                                                                                                                                                                                                                                                                 |
+-----------------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| menuPosition                | String  | "fixed" | "scrollable"                                                                                                            | Sets the menu position. Scrollable would makes both the menus scrollable with body element.                                                                                                                                                                                                                           |
+-----------------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sidebar                     | Object  | { "color": "light" | "dark" | "brand" | "gradient",      "size": "default" | "condensed" | "compact", "showuser": true | false }  | The left sidebar related configuration. It's nested object. The color can be set to "light", "dark", "brand" or "gradient". The size would allow to change the size of sidebar to condensed (coompact) or even more small by setting "compact". The showuser, if set to true, would display a user in left sidebar    |
+-----------------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| topbar                      | Object  | { "color": "light" | "dark" }                                                                                                     | The topbar related configuration. It's nested object. The color can be set to "light", "dark", "brand" or "gradient".                                                                                                                                                                                                 |
+-----------------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| showRightSidebarOnPageLoad  | Boolean | true | false                                                                                                                      | Indicates whether to show right sidebar on opening up the page                                                                                                                                                                                                                                                        |
+-----------------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Following are few examples:

- Changes the left sidebar theme to "Dark"
.. code:: html
    
        <body class="loading" data-layout='{"sidebar": { "color": "dark"}}'></body>
    
- Changes the left sidebar theme to "Light (White)"
.. code:: html
    
        <body class="loading" data-layout='{"sidebar": {"color": "light"}}'></body>

- Sets the menus (left sidebar and topbar) scrollable with body
.. code:: html
    
        <body class="loading" data-layout='{"menuPosition": true}'></body>

- Changes the left sidebar size to small
.. code:: html
    
        <body class="loading" data-layout='{"sidebar": {"size": "compact"}}'></body>

- Changes the topbar color to light (white)
.. code:: html
    
        <body class="loading" data-layout='{"topbar": {"color": "light"}}'></body>

- Changes the overall color mode to dark
.. code:: html
    
        <body class="loading" data-layout='{"mode": "dark"}'></body>


-------------------------------------------

RTL Version
------------

**Light Version**:

In order to have RTL enabled with light version, replace the reference of ``bootstrap.min.css`` stylesheet file to ``bootstrap-rtl.min.css`` and ``app.min.css`` to ``app-rtl.min.css``

**Dark Version**:

In order to have RTL enabled with dark version, replace the reference of ``bootstrap.min.css`` stylesheet file to ``bootstrap-dark-rtl.min.css`` and ``app.min.css`` to ``app-dark-rtl.min.css``