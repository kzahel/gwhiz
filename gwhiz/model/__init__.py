"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm, schema, types
import os
from gwhiz.model import meta


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine

publication_table = schema.Table('publication', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('seq_id', optional=True), primary_key=True),
    schema.Column('type', types.Unicode(255)),
    schema.Column('title', types.Unicode(255)),
    schema.Column('catalog_number', types.Unicode(255)),
    schema.Column('isbn_number', types.Unicode(255)),
    schema.Column('website', types.Text()),
    schema.Column('price', types.Numeric),
    schema.Column('featured', types.Boolean,default=False),
    schema.Column('incomplete', types.Boolean,default=False),
    schema.Column('description', types.UnicodeText()),
    schema.Column('blurb', types.Text),
    schema.Column('image', types.Text()) )

work_table = schema.Table('work', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('work_seq_id', optional=True), primary_key=True),
    schema.Column('title', types.Unicode(255)),
    schema.Column('keyid', types.Integer, schema.ForeignKey('key.id')),
    schema.Column('composerid', types.Integer, schema.ForeignKey('composer.id')),
    schema.Column('description', types.UnicodeText()),
    schema.Column('price', types.Numeric),
    schema.Column('pages', types.Numeric),
    schema.Column('featured', types.Boolean,default=False),
    schema.Column('blurb', types.Text),
    schema.Column('image', types.Text()) )

key_table = schema.Table('key', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('key_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)) )

musiccredit_table = schema.Table('musiccredit', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('musiccredit_seq_id', optional=True), primary_key=True),
    schema.Column('composerid', types.Integer, schema.ForeignKey('composer.id')),
    schema.Column('image', types.Text()),
    schema.Column('description', types.UnicodeText()),
    schema.Column('name', types.Unicode(255)) )

instrument_table = schema.Table('instrument', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('instrument_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)) )

style_table = schema.Table('style', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('style_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)) )

movement_table = schema.Table('movement', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('movement_seq_id', optional=True), primary_key=True),
    schema.Column('title', types.Unicode(255)),
    schema.Column('keyid', types.Integer, schema.ForeignKey('key.id')),
    schema.Column('number', types.Integer),
    schema.Column('workid', types.Integer, schema.ForeignKey('work.id')),
    schema.Column('description', types.UnicodeText()) )

composer_table = schema.Table('composer', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('composer_seq_id', optional=True), primary_key=True),
    schema.Column('lastname', types.Unicode(255)),
    schema.Column('firstname', types.Unicode(255)),
    schema.Column('middlename', types.Unicode(255)),
    schema.Column('bio', types.UnicodeText()),
    schema.Column('email', types.Text()),
    schema.Column('website', types.Text()),
    schema.Column('image', types.Text()) )

artist_table = schema.Table('artist', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('composer_seq_id', optional=True), primary_key=True),
    schema.Column('lastname', types.Unicode(255)),
    schema.Column('firstname', types.Unicode(255)),
    schema.Column('middlename', types.Unicode(255)),
    schema.Column('bio', types.UnicodeText()),
    schema.Column('email', types.Text()),
    schema.Column('website', types.Text()),
    schema.Column('image', types.Text()) )

soundclip_table = schema.Table('soundclip', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('soundclip_seq_id', optional=True), primary_key=True),
    schema.Column('workid', types.Integer, schema.ForeignKey('work.id')),
    schema.Column('movementid', types.Integer, schema.ForeignKey('movement.id')),
    schema.Column('path', types.Text()) )

workinstrument_table = schema.Table('workinstrument', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('workinstrument_seq_id', optional=True), primary_key=True),
    schema.Column('workid', types.Integer, schema.ForeignKey('work.id')),
    schema.Column('instrumentid', types.Integer, schema.ForeignKey('instrument.id')),
)
workstyle_table = schema.Table('workstyle', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('workstyle_seq_id', optional=True), primary_key=True),
    schema.Column('workid', types.Integer, schema.ForeignKey('work.id')),
    schema.Column('styleid', types.Integer, schema.ForeignKey('style.id')),
)
workpublication_table = schema.Table('workpublication', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('seq_id', optional=True), primary_key=True),
    schema.Column('workid', types.Integer, schema.ForeignKey('work.id')),
    schema.Column('publicationid', types.Integer, schema.ForeignKey('publication.id')),
)
movementpublication_table = schema.Table('movementpublication', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('seq_id', optional=True), primary_key=True),
    schema.Column('movementid', types.Integer, schema.ForeignKey('movement.id')),
    schema.Column('publicationid', types.Integer, schema.ForeignKey('publication.id')),
)
publicationstyle_table = schema.Table('publicationstyle', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('seq_id', optional=True), primary_key=True),
    schema.Column('publicationid', types.Integer, schema.ForeignKey('publication.id')),
    schema.Column('styleid', types.Integer, schema.ForeignKey('style.id')),
)
publicationartist_table = schema.Table('publicationartist', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('seq_id', optional=True), primary_key=True),
    schema.Column('publicationid', types.Integer, schema.ForeignKey('publication.id')),
    schema.Column('artistid', types.Integer, schema.ForeignKey('artist.id')),
)
publicationcomposer_table = schema.Table('publicationcomposer', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('seq_id', optional=True), primary_key=True),
    schema.Column('publicationid', types.Integer, schema.ForeignKey('publication.id')),
    schema.Column('composerid', types.Integer, schema.ForeignKey('composer.id')),
)
publicationinstrument_table = schema.Table('publicationinstrument', meta.metadata,
    schema.Column('id', types.Integer, schema.Sequence('seq_id', optional=True), primary_key=True),
    schema.Column('publicationid', types.Integer, schema.ForeignKey('publication.id')),
    schema.Column('instrumentid', types.Integer, schema.ForeignKey('instrument.id')),
)

class Publication(object):
    def __repr__(self):
        return '<%s(%s, price=%s)'%(self.__class__.__name__,self.liststring(),self.getprice())
    def getlink(self):
        return '/catalog/publicationdetail/%i'%self.id
    def getblurb(self):
        if self.blurb:
            return self.blurb
        elif self.works:
            return self.works[0].blurb
    def cartstring(self):
        return 'Publication-%i'%self.id
    def liststring(self):
        if self.title:
            return self.title
        else:
            if len(self.works) == 1:
                return self.works[0].liststring()
    def gettitle(self):
        return self.liststring()
    def getstyles(self):
        if len(self.styles) == 0:
            styles = []
            return self.works[0].styles
            for w in self.works:
                styles += w
            return styles
        else:
            return self.styles
    def getprice(self):
        if self.price:
            return self.price
        price = 0
        for thing in self.works + self.movements:
            if thing.price:
                price += thing.price
        if price == 0:
            return 10
        else:
            return price



class Work(object):
    def __repr__(self):
        return '<Work: %s>'%self.title
    def liststring(self):
        return self.title

class Key(object):
    def __repr__(self):
        return '<Key: %s>'%self.name
    def liststring(self):
        return self.name
    def imagetag(self):
        return '<img src="/keys/%s.png" alt="%s">'%(keydic[self.name],self.name)

class Instrument(object):
    def __repr__(self):
        return '<Instrument: %s>'%self.name
    def liststring(self):
        return self.name
    def imagetag(self):
        return '<img src="/instruments/icon/%s.png" alt="%s">'%(self.name,self.name)

class Style(object):
    def __repr__(self):
        return '<Style: %s>'%self.name
    def liststring(self):
        return self.name

class Movement(object):
    def __repr__(self):
        return '<Movement: %s>'%self.title
    def liststring(self):
        if self.description:
            if len(self.description) > 60:
                desc = self.description[60:]
            else:
                desc = self.description
            return '%s - %s'%(self.title, desc)
        else:
            return self.title

class Composer(object):
    def __repr__(self):
        return '<Composer: %s, %s>'%(self.lastname, self.firstname)
    def previewimage(self):
        path,filename = os.path.split(self.image)
	return path+'/' + '.'+filename
    def fullname(self):
        if self.middlename:
            return '%s %s %s'%(self.firstname, self.middlename, self.lastname)
        else:
            return '%s %s'%(self.firstname, self.lastname)
    def liststring(self):
        return self.fullname()
    def imagetag(self):
        #detaillink = '/composers/view/%s'%self.id
        #return '<a href="%s"><img src="%s" alt="%s"></a>'%(detaillink,self.image,self.fullname())
        return '<img src="%s" alt="%s">'%(self.image, self.fullname())


class Artist(object):
    def __repr__(self):
        return '<Artist: %s>'%self.fullname()
    def imagetag(self):
        return '<img src="%s" alt="%s">'%(self.image, self.fullname())
    def fullname(self):
        if self.middlename:
            return '%s %s %s'%(self.firstname, self.middlename, self.lastname)
        else:
            return '%s %s'%(self.firstname, self.lastname)


class Soundclip(object):
    def __repr__(self):
        return '<Soundclip: %s>'%self.path

class MusicCredit(object):
    def __repr__(self):
        return '<MusicCredit: %s>'%self.name

orm.mapper(MusicCredit, musiccredit_table)

orm.mapper(Work, work_table, properties={
   'movements':orm.relation(Movement, backref='work'),
   'soundclips':orm.relation(Soundclip, backref='work'),
   'instruments':orm.relation(Instrument, secondary=workinstrument_table),
   'styles':orm.relation(Style, secondary=workstyle_table),
   'publications':orm.relation(Publication, secondary=workpublication_table),
})

orm.mapper(Movement, movement_table, properties={
   'soundclips':orm.relation(Soundclip, backref='movement'),
   'publications':orm.relation(Publication, secondary=movementpublication_table)
})

orm.mapper(Soundclip, soundclip_table)

orm.mapper(Composer, composer_table, properties={
    'works':orm.relation(Work, backref='composer'),
    'musiccredits':orm.relation(MusicCredit, backref='composer'),
    'publications':orm.relation(Publication, secondary=publicationcomposer_table),
})

orm.mapper(Style, style_table, properties={
    'works':orm.relation(Work, secondary=workstyle_table),
    'publications':orm.relation(Publication, secondary=publicationstyle_table),
})

orm.mapper(Artist, artist_table, properties={
    'publications':orm.relation(Publication, secondary=publicationartist_table),
})

orm.mapper(Publication, publication_table, properties={
    'works':orm.relation(Work, secondary=workpublication_table),
    'movements':orm.relation(Movement, secondary=movementpublication_table),
    'composers':orm.relation(Composer, secondary=publicationcomposer_table),
    'artists':orm.relation(Artist, secondary=publicationartist_table),
    'styles':orm.relation(Style, secondary=publicationstyle_table),
    'works':orm.relation(Work, secondary=workpublication_table),
    'instruments':orm.relation(Instrument, secondary=publicationinstrument_table),
})



orm.mapper(Instrument, instrument_table, properties={
    'works':orm.relation(Work, secondary=workinstrument_table),
})

orm.mapper(Key, key_table, properties={
    'works':orm.relation(Work, backref='key'),
    'movements':orm.relation(Movement, backref='key'),
})

##### navigation
nav_table = schema.Table('nav', meta.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('nav_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255), default=u'Untitled Node'),
    schema.Column('path', types.Unicode(255), default=u''),
    schema.Column('parentid', types.Integer(), schema.ForeignKey('nav.id')),
    schema.Column('nextid', types.Integer(), default=None),
    schema.Column('type', types.String(30))
)

class Nav(object):
    def __repr__(self):
        return '<Nav: %s>'%self.name

#orm.mapper(Nav, nav_table)
orm.mapper(Nav, nav_table, properties={
    'children': orm.relation(Nav, backref=orm.backref('parent', remote_side=[nav_table.c.id]))
})

keydic = {}
keydic['Atonal'] = '0'
keydic['C major'] = '0'
keydic['A minor'] = '0'
keydic['F major'] = '1f'
keydic['D minor'] = '1f'
keydic['G major'] = '1s'
keydic['E minor'] = '1s'
keydic['B flat major'] = '2f'
keydic['G minor'] = '2f'
keydic['D major'] = '2s'
keydic['B minor'] = '2s'
keydic['E flat major'] = '3f'
keydic['C minor'] = '3f'
keydic['A major'] = '3s'
keydic['F sharp minor'] = '3s'
keydic['A flat major'] = '4f'
keydic['F minor'] = '4f'
keydic['E major'] = '4s'
keydic['C sharp minor'] = '4s'
keydic['D flat major'] = '5f'
keydic['B flat minor'] = '5f'
keydic['B major'] = '5s'
keydic['G sharp minor'] = '5s'
keydic['G flat major'] = '6f'
keydic['E flat minor'] = '6f'
keydic['F sharp major'] = '6s'
keydic['D sharp minor'] = '6s'
keydic['C flat major'] = '6f'
keydic['A flat minor'] = '6f'
keydic['C sharp major'] = '6s'
keydic['A sharp minor'] = '6s'
