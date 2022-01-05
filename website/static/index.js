function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteMethane(methaneId) {
  fetch("/delete-methane", {
    method: "POST",
    body: JSON.stringify({ methaneId: methaneId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}