function confirmDelete(event) {
    event.preventDefault()


    if (confirm("Are you sure you want to delete this ticket?")) {
      event.target.parentElement.submit()
    }
}