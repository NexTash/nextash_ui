(() => {
  // frappe-html:/home/fasi/bench-14/apps/nextash/nextash/public/js/ui/toolbar/navbar.html
  frappe.templates["navbar"] = `<header class="navbar navbar-expand sticky-top" role="navigation">
  <div class="container">
    <a class="navbar-brand navbar-home" href="/app">
      <img
        class="app-logo"
        style="width: {{ navbar_settings.logo_width || 24 }}px"
        src="/assets/nextash/images/nextash-logo.png"
      />
    </a>
    <ul class="nav navbar-nav d-none d-sm-flex" id="navbar-breadcrumbs"></ul>
    <div class="collapse navbar-collapse justify-content-end">
      <form
        class="form-inline fill-width justify-content-end"
        role="search"
        onsubmit="return false;"
      >
        <div class="input-group search-bar text-muted hidden">
          <input id="navbar-search" type="text" class="form-control"
          placeholder="{%= __("Search or type a command (Ctrl + G)") %}"
          aria-haspopup="true" >
          <span class="search-icon">
            <svg class="icon icon-sm">
              <use xlink:href="#icon-search"></use>
            </svg>
          </span>
        </div>
      </form>
      <ul class="navbar-nav">
        <li
          class="nav-item dropdown dropdown-notifications dropdown-mobile hidden"
        >
          <a
            class="nav-link notifications-icon text-muted"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="true"
            href="#"
            onclick="return false;"
          >
            <span class="notifications-seen">
              <svg class="icon icon-md">
                <use href="#icon-notification"></use>
              </svg>
            </span>
            <span class="notifications-unseen">
              <svg class="icon icon-md">
                <use href="#icon-notification-with-indicator"></use>
              </svg>
            </span>
          </a>
          <div
            class="dropdown-menu notifications-list dropdown-menu-right"
            role="menu"
          >
            <div class="notification-list-header">
              <div class="header-items"></div>
              <div class="header-actions"></div>
            </div>
            <div class="notification-list-body">
              <div class="panel-notifications"></div>
              <div class="panel-events"></div>
            </div>
          </div>
        </li>
        <li class="nav-item dropdown dropdown-message dropdown-mobile hidden">
          <a
            class="nav-link notifications-icon text-muted"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="true"
            href="#"
            onclick="return false;"
          >
            <span>
              <svg class="icon icon-md">
                <use href="#icon-small-message"></use>
              </svg>
            </span>
          </a>
        </li>
        <li class="vertical-bar d-none d-sm-block"></li>
        <li
          class="nav-item dropdown dropdown-help dropdown-mobile d-none d-lg-block"
        >
          <a
            class="nav-link"
            data-toggle="dropdown"
            href="#"
            onclick="return false;"
          >
            {{ __("Help") }}
            <span>
              <svg class="icon icon-xs">
                <use href="#icon-small-down"></use>
              </svg>
            </span>
          </a>
          <div
            class="dropdown-menu dropdown-menu-right"
            id="toolbar-help"
            role="menu"
          >
            <div id="help-links"></div>
            <div class="dropdown-divider documentation-links"></div>
            {% for item in navbar_settings.help_dropdown %} {% if (!item.hidden)
            { %} {% if (item.item_label != "Documentation") { %} {% if
            (item.item_label != "About") { %} {% if (item.item_label != "User
            Forum") { %} {% if (item.route) { %}
            <a class="dropdown-item" href="{{ item.route }}">
              {%= __(item.item_label) %}
            </a>
            {% } else if (item.action) { %}
            <a class="dropdown-item" onclick="return {{ item.action }}">
              {%= __(item.item_label) %}
            </a>
            {% } else { %}
            <div class="dropdown-divider"></div>
            {% } %} {% } %} {% } %} {% } %} {% } %} {% endfor %}
          </div>
        </li>
        <li class="nav-item dropdown dropdown-navbar-user dropdown-mobile">
          <a
            class="nav-link"
            data-toggle="dropdown"
            href="#"
            onclick="return false;"
          >
            {{ avatar }}
          </a>
          <div
            class="dropdown-menu dropdown-menu-right"
            id="toolbar-user"
            role="menu"
          >
            <a class="dropdown-item" id="employee-checkin">Employee Checkin</a>
            <a class="dropdown-item" id="employee-checkout">Employee CheckOut</a>

            {% for item in navbar_settings.settings_dropdown %} {% if
            (!item.hidden) { %} {% if (item.item_label != "Toggle Theme") { %}
            {% if (item.route) { %}
            <a class="dropdown-item" href="{{ item.route }}">
              {%= __(item.item_label) %}
            </a>
            {% } else if (item.action) { %}
            <a class="dropdown-item" onclick="return {{ item.action }}">
              {%= __(item.item_label) %}
            </a>
            {% } else { %}
            <div class="dropdown-divider"></div>
            {% } %} {% } %} {% } %} {% endfor %}
          </div>
        </li>
      </ul>
    </div>
  </div>
</header>

`;

  // ../nextash/nextash/public/js/ui/toolbar/issue-report.js
  $(document).bind("toolbar_setup", function() {
    const $report_to = $('a[href="https://github.com/frappe/erpnext/issues"]');
    $report_to.attr("href", "javascript:void(0)");
    $report_to.addClass("showHelpDialog");
  });
  $(document).on("click", ".showHelpDialog", function() {
    new frappe.views.CommunicationComposer({
      doc: {},
      subject: "Report Issue",
      recipients: "support@nextash.com"
    });
  });

  // ../nextash/nextash/public/js/navbar.js
  $(document).on("click", "#employee-checkin", function() {
    frappe.call({
      method: "nextash.events.employee_checkin.employee_checkin",
      args: {},
      callback: function(r) {
        if (!r.exc) {
          frappe.show_alert({
            message: __("Your attendence has been Marked"),
            indicator: "green"
          }, 5);
          $("#employee-checkin").hide();
          $("#employee-checkout").show();
        }
      }
    });
  });
  $(document).on("click", "#employee-checkout", function() {
    frappe.call({
      method: "nextash.events.employee_checkin.employee_checkout",
      args: {},
      callback: function(r) {
        if (!r.exc) {
          frappe.show_alert({
            message: __("Your attendence has been Marked"),
            indicator: "green"
          }, 5);
          $("#employee-checkin").show();
          $("#employee-checkout").hide();
        }
      }
    });
  });
  $(document).ready(function() {
    frappe.call({
      method: "nextash.events.employee_checkin.check_status",
      args: {},
      callback: function(r) {
        if (r.message == true) {
          $("#employee-checkin").hide();
          $("#employee-checkout").show();
        } else if (r.message == false) {
          $("#employee-checkin").show();
          $("#employee-checkout").hide();
        } else {
          $("#employee-checkin").hide();
          $("#employee-checkout").hide();
        }
      }
    });
    ;
  });
})();
//# sourceMappingURL=toolbar.bundle.SNVNTVK3.js.map
