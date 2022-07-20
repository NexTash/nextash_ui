frappe
  .call("nextash.api.theme_settings.auth.get_auth_slogan")
  .then((r) => {
    const res = r.message;
    let auth_logo = res.auth_logo;
    let auth_title = res.auth_title;
    let auth_text = res.auth_text;

    if (!auth_logo) {
      auth_logo = "/assets/nextash/images/nextash.jpg";
    }

    if (!auth_title) {
      auth_title = "Nextash";
    }

    if (!auth_text) {
      auth_text = "Simple Solutions for Complex Connections.";
    }

    $(".no-auth-page-logo").attr("src", auth_logo);
    $(".no-auth-page-brand").html(auth_title);
    $(".page-custom-title").html(auth_text);
  });
