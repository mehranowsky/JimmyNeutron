function gau(){
const keyword = 'COMPANY_NAME';
urls = []
$$('*').forEach(element => {
  urls.push(element.src)
  urls.push(element.href)
  urls.push(element.url)
}); 
const links = [...new Set(urls)];
const filteredUrls = [];

for (let u of links) {
if (typeof u === 'string') {
    let find = u.search(keyword);
    if (find >= 0) {
        filteredUrls.push(u);
    }
}
}

console.log("Found URLs:", filteredUrls);

}
gau()
