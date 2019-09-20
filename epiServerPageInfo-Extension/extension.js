javascript: (function() {
  function displayData(text) {
    body = document.getElementsByTagName("BODY")[0];
    child = document.createElement("div");
    child.innerHTML = text;
    child.style.color = "red";
    child.style.backgroundColor = "yellow";
    body.insertBefore(child, body.firstChild);
  }
  try {
    pageID = $("input[name='_epi_page_id']").val();
    pageID = `EpiServer Page ID: ${pageID}`;
    displayData(pageID);
  } catch (err) {
    console.error(err);
  }
  try {
    brm = $("input[name='_br_api_request']").val();
    brm = brm
      .replace("account_id=x", "account_id=5221")
      .replace("auth_key=x", "auth_key=o5xlkgn7my5fmr5c")
      .replace("start=d+", "start=0")
      .replace("/user_agent=(.+?)&/", "")
      .replace("/user_ip=(.+?)&/", "")
      .replace("/ref_url=(.+?)&/", "")
      .replace("rows=d+", "rows=5000");
    brm = `<a style="color:blue;" href=${brm}>Bloomreach API Link</a>`;
    displayData(brm);
  } catch (err) {
    console.error(err);
  }
  displayData(
    "<h4><i>Pretty Average Not Terrible Enquiry Running Algorithm</i></h4>"
  );
  displayData("<h1>PANTERA</h1>");
})();
