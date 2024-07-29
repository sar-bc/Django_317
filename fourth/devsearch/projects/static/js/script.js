   let searchFrom = document.getElementById('search');
   let pageLinks = document.querySelectorAll('.page-link');

   if (searchFrom){
    for (let  i=0; pageLinks.length > i; i++){
      pageLinks[i].addEventListener("click", function(event){
        event.preventDefault();

        let page = this.dataset.page;

        searchFrom.innerHTML += `<input value=${page} name='page' type='hidden'>`;

        searchFrom.submit();
      })
    }
   }