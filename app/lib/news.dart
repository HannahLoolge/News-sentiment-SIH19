class News {
  String title; //
  String dateTime; //
  String source; //
  String url; //
  int score; //
  String sentiment;
  int id;
  String imageUrl;
  String category;

  News(
      {this.id,
        this.url,
      this.dateTime,
      this.score,
      this.sentiment,
      this.source,
      this.title,this.category,
      this.imageUrl});

}
