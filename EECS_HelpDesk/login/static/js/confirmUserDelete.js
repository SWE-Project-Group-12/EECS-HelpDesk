function confirmUserDelete(event) {
    
    
    if (!confirm("Are you sure you want to delete this user?")) {
        event.cancelBubble = true 
        event.stopPropagation = true
        event.preventDefault()
    }
}