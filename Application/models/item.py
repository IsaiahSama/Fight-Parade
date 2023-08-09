"""File to store the item model and information."""
from .extensions import db 

class BaseItem(db.Model):
    """Base class for all Items (Item, Gear and Skills)"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(70))
    tooltip = db.Column(db.String(50))
    effect = db.Column(db.String(150))
    cost = db.Column(db.Integer)
    tier = db.Column(db.Integer)
    reborn = db.Column(db.Integer)
    item_type = db.Column(db.String(30))
    img_url = db.Column(db.String(100))


    def get_str(self):
        return f"""<div class="itemCard card">
  <div class="card-image">
    <center>
      <img src="{ self.img_url }" alt="" width="50px" height="50px" />
    </center>
  </div>
  <div class="card-header" style="flex-direction: column">
    <div class="card-header-title is-centered">
      <p>{ self.name } </p>
    </div>
    <div class="media-content" style="padding:0.5em;>
      <p class="subtitle is-6"> { self.tooltip } </p>
      <p class="subtitle is-7"> {self.description} </p>
    </div>
  </div>
  <div class="card-footer">
    <p class="card-footer-item">Price:<br>{ self.cost }₱</p>
    <p class="card-footer-item">ID:<br>{ self.id }</p>
    <p class="card-footer-item">Tier:<br>{ self.tier }</p>
    <p class="card-footer-item">Type:<br> { self.item_type }</p>
  </div>
</div>"""

class Item(BaseItem):
    """Class used to rerpresent consumable items"""

    id = db.Column(db.Integer, db.ForeignKey('base_item.id'), primary_key=True)
    duration = db.Column(db.Integer)

