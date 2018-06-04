function setTable() {

    var table = document.getElementById('table');
    $.ajax({
      type: "GET",
      url: '/ajax/submissions',
      success: function(json) {
          var html = "";
          html += "<table class=\"table\">";
          html += "<thead><tr><th scope=\"col\">Matrícula</th><th scope=\"col\">Data/Hora</th><th scope=\"col\">Avaliação</th><th scope=\"col\">Acerto (%)</th></tr></thead><tbody>";
          for (var i = 0; i < json.submissions.length; i++) {
              var submission = json.submissions[i];
              html += "<tr>";
              html += "<td>" + submission.registration + "</td>";
              html += "<td>" + moment(submission.date).format("DD/MM/YYYY HH:mm") + "</td>";
              html += "<td>" + submission.evaluation + "</td>";
              html += "<td>" + submission.grade + "</td>";
              html += "</tr>";
          }
          html += "  </tbody></table>";
          table.innerHTML = html;
      }
    })
}