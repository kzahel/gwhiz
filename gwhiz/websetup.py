# -*- coding: utf-8 -*-
"""Setup the gwhiz application"""
import logging

from gwhiz.config.environment import load_environment
from gwhiz.model import meta
from gwhiz import model
from authkit.users.sqlalchemy_driver import UsersFromDatabase


log = logging.getLogger(__name__)

log.info("Adding the AuthKit model...")
users = UsersFromDatabase(model)

print 'hi';
def setup_app(command, conf, vars):
    """Place any commands to setup gwhiz here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    meta.metadata.create_all(bind=meta.engine)

    log.info("Adding roles and uses...")
    users.role_create("delete")
    users.user_create("gwhiz", password="bontin")
    users.user_create("admin", password="bontin")
    users.user_add_role("admin", role="delete")

    a = model.Artist()
    a.firstname = 'Jeri-Mae'
    a.middlename = 'G'
    a.lastname = 'Astolfi'
    meta.Session.add(a)


    a = model.Artist()
    a.firstname = 'Enrico'
    a.middlename = ''
    a.lastname = 'Pompili'
    meta.Session.add(a)

    a = model.Artist()
    a.firstname = 'Gabriele'
    a.middlename = ''
    a.lastname = 'Baldocci'
    meta.Session.add(a)


    r = model.Artist()
    r.firstname = 'Roberto'
    r.middlename = ''
    r.lastname = 'Prosseda'
    r.website = 'http://www.robertoprosseda.com/'
    r.bio = """Born in Latina, Italy, in 1975, Roberto Prosseda studied at the Accademia Pianistica "Incontri col Maestro" of Imola with Alexander Lonquich, Boris Petrushansky and Franco Scala and at the International Piano Foundation in Cadenabbia (Lake Como, Italy) with Dmitri Bashkirov, Leon Fleisher, William Grant Naboré, Charles Rosen, Karl Ulrich Schnabel, Fou Ts'ong.

After winning major prizes in several important piano competitions, including the "U. Micheli" in Milan, the "F. Schubert" in Dortmund, the "A.Casagrande" in Terni and the "W.A.Mozart" in Salzburg, Roberto Prosseda has performed in Europe, Asia, Australia, North and South America. His recent engagements include Berlin Philharmonie, Leipzig Gewandhaus, Wigmore Hall, Kuhmo Chamber Music Festival, Maggio Musicale Fiorentino, Teatro alla Scala and Sala Verdi in Milano, Festival Pianistico di Bergamo e Brescia, Settembre Musica in Torino, Ravenna Festival, Triennale Köln, Biennale di Venezia.

Roberto Prosseda has appeared as a soloist with many orchestras, like Filarmonica della Scala, Philarmonie der Nationen, Bochumer Symphoniker, Oriol Ensemble, Wiener Kammerorchester, Mozarteum Orchester, Orchestra di Padova e del Veneto, Mozart Festival Orchestra, Kammerakademie-Potsdam, Orchestra della Toscana, Filarmonica di Torino, Santa Cecilia di Roma."""
    r.image = '/images/prosseda.jpg'
    meta.Session.add(r)

    michael = model.Composer()
    michael.website = 'http://www.michaelglennwilliams.com'
    michael.email = 'composer@music.org'
    michael.firstname = 'Michael'
    michael.middlename = 'Glenn'
    michael.lastname = 'Williams'
    michael.image = '/michael_headshot.jpg'
    michael.bio = """
 Michael Glenn Williams composes for a wide range of musical styles and purposes, from prize winning contemporary symphonic concert music, concert choir, chamber and solo piano works to avant-garde electronic music, Christian, Hebrew and popular songwriting, jazz, television and film. His jazz group "1 40 4 20" has released two publications: "Jazz Trespassers" and "Wet", to critical acclaim. Michael G. Williams' music and piano performance is featured on the recent films "Wonderland" and "The Limey" from Universal Pictures.

As a columnist, his articles have appeared in IEICE, Electronic Music Educator, Klavier and Computer Music Journal. Michael G. Williams is well known in the computer industry as an expert in operating system design, system hardware design and computer chip functional design. He serves full time as a Principal Architect for Nokia's Office of the CTO. He was the author of the music, MIDI sequencing, typesetting and printing program SuperScore, and consulted on the design of the original music font for general use "Sonata" with Adobe Systems. His name appears in three IEEE international computer standards.

Michael Williams has served as a director on the board of the Thousand Oaks Philharmonic, national Treasurer for NACUSA, director of contemporary music at Ascension Lutheran Church in Thousand Oaks, and for the Rothstein conservative temple in Woodland Hills, CA. He has served as accompanist or organist for numerous churches, temples, colleges and master classes in Southern California. As an accomplished classical pianist, Michael Williams twice won the Northridge Chamber Music award, and has premiered works written for him by composers such as Jeffery Cotton and Jeff Rona. He was recently guest artist at the first national conference of NACUSA in Kansas City, 2003. He performs with the Chopin Project, a group of pianists performing scholarly and unusual concerts of Chopin.

Michael Williams has composed five musicals for children and youth; music for the television series "Chicago Hope"; scored scenes for movies such as "The Limey", "King of the Hill", "Younger and Younger", "House of Yes" and "Wonderland"; two piano concertos, a trio for the Westlake Chamber Ensemble; a string quartet for the Escher Quartet; over sixty songs for use in Christian worship; over forty songs for his instrumental jazz group; a symphony and concert march for symphonic band; an orchestral tone poem; and numerous contemporary pieces for solo piano. An publication of his solo piano music was recorded by Roberto Prosseda for AIX Media Group. An publication of solo and duo piano music was recorded by Enrico Pompili and Gabrielle Baldocci for the Stradivarius Records label, to be released in 2008.

Mr. Williams taught music composition at UCLA extension. He studied composition and piano performance at California State University Northridge and at the Eastman School of Music, where he won the Howard Hanson Prize for orchestral composition. He lives in Ventura County, California.
    """
    meta.Session.add(michael)

    c = model.Composer()
    c.firstname = 'Sergio'
    c.middlename = ''
    c.lastname = 'Cafaro'
    c.image = '/cafaro.gif'
    c.bio = """
Sergio Cafaro, born in Rome, graduated in piano at the Conservatorio di S. Cecilia of the same city under the guidance of Rodolfo Caporali and in composition under the guidance of Goffredo Petrassi. Winner of many national and international piano competitions, among them the Competition in Genève, he began his concert career playing for the most important Italian societies. His repertoire includes many works from the piano literature from the 18th to the 20th century, with particular reference to Mozart, Schubert, Schumann and Debussy. He has performed with many well-known violinists, including Milstein, Szering and Carminelli and under the direction of Stravinsky, Hindemith, Boulez and Petrassi.

He composed several symphonic, chamber and piano compositions that are performed in many countries of Europe, Asia, North and South America. He was the reviser for many of the Rossini piano works, a collaborator of radio programming for the third channel of RAI as well as Radio Vaticana and collaborator of several musical journals. He has recorded CDs for Edipan.

Cafaro is often called as a jury member for national and international piano competitions. He held masterclasses in many schools and academies; among them AMOR, Accademia Musicale Pescarese and the Campus Internazionale di Sermoneta. He began teaching in 1956 at the Conservatorio Rossini di Pescara, was professor of piano at the Conservatorio di S. Cecilia di Roma and now is an instructor at the Accademia AIDA.
    """
    meta.Session.add(c)


    c = model.Composer()
    c.firstname = 'Lorenzo'
    c.middlename = ''
    c.lastname = 'Salvagni'
    c.image = '/salvagni.jpg'
    c.bio = """

      Lorenzo Salvagni is a native of Rome, Italy, where he received degrees from the Conservatorio O. Respighi in piano and St. Cecilia in Chamber Music. He has also studied with Rosalyn Turek, Charles Rosen, Robert Levine, Sergio Fiorentino and Benedetto Lupo. He has done special studies in organ and composition and has an Arts Degree from the University of Rome.

      Salvagni worked for one year as a press agent for the School of Music of Fiesole, in Florence, then moved to Milan, where he pursued a one-year Master in Communication at the Catholic University there. Immediately after receiving this degree, he was hired for one year of internship by Suonare, one of the premier classical music magazines in Italy. While there, he published many articles for the magazine.

      Lorenzo has also earned a Master of Music degree in Collaborative Piano at the Cleveland Institute of Music, where he studied with Anita Pontremoli. In Cleveland, he is coordinator of the Contemporary Ensemble at Holy Rosary Church, Associate Music Director at the Church of St. Mary in Olmsted Falls and an accompanist at the Cleveland Music School Settlement.

      He has also been working as an Italian Lecturer at Case Western Reserve University in Cleveland for the past two years.

      As a translator and language consultant, Lorenzo has collaborated with the Cleveland Orchestra in the production of Verdi's Falstaff (2006) and Grieg's Peer Gynt (2007). In august 2007 Lorenzo has given a lecture on Italian folk music at the Cleveland Museum of Natural History, part of the anthropology of music series.

      Lorenzo's piece for flute and piano Gigallegro! was composed in 2007 and selected by the Greater Cleveland Flute Society to be performed in a concert dedicated to local composers.

      Lorenzo Salvagni recorded his debut CD performing with flutist Maurizio Bignardelli on Italy's Inedita label.

    """
    meta.Session.add(c)


    for note in 'C,D,E,F,G,A,B'.split(','):
        for accidental in ',sharp,flat'.split(','):
            for mode in 'major,minor'.split(','):
                key = model.Key()
                if accidental:
                    key.name = '%s %s %s'%(note,accidental,mode)
                else:
                    key.name = '%s %s'%(note,mode)
                meta.Session.add(key)
    key = model.Key()
    key.name = 'Atonal'
    meta.Session.add(key)

    for name in 'Voice,Orchestra,Piano,Organ,Flute,Oboe,Clarinet,Bassoon,Trumpet,French horn,Trombone,Double bass,Cello,Viola,Violin,Percussion,Tuba,Timpani,Saxophone,Guitar,Soprano,Tenor'.split(','):
        instr = model.Instrument()
        instr.name = name
        meta.Session.add(instr)

    for stylename in 'Classical,Modern,Jazz,Film,Chamber Music,Television,Musical Theater,Popular Song,Arrangement,Vocal'.split(','):
        style = model.Style()
        style.name = stylename
        meta.Session.add(style)



    work = model.Work()
    work.title = 'Gigallegro'
    work.blurb = 'For flute and piano'
    work.description = """
    Composed in 2007, Gigallegro was originally conceived as a piano etude, which explains the dense piano writing that requires a solid technique and a very light touch not to overpower the flute. This 10 minutes, one-movement piece has two sections, the first one (allegro) can be roughly defined as a sonata form with some licenses; the second one has the character of a gigue (giga). The two terms combined form the title of the piece: giga-allegro.

Gigallegro’s first performance took place on Friday, November 9th, 2007, at Harkness Chapel in Cleveland. The piece was later selected by the Greater Cleveland Flute Society to be included in the program of the 2008 edition of “Cleveland Composers Connection” and performed on April 27th, 2008, at Judson Manor in Cleveland.

Gigallegro is now being published in the United States by Gwhiz Arts and Sciences. """
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Lorenzo').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    i = meta.Session.query(model.Instrument).filter_by(name='Flute').one()
    work.instruments.append( i )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-LS01-1001'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)



    # ---
    work = model.Work()
    work.title = 'Vive Carmen!'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.key = meta.Session.query(model.Key).filter_by(name='E flat major').one()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Sergio').one()
    work.image = '/vivecarmen.gif'
    work.description = """
Vive Carmen has been featured in performances on Italian radio and television, and on tour with Alessandra Amarra and Roberto Prosseda, and Gabriele Baldocci and Martha Argerich.
    """
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-SC01-1001'
    p.composers.append( meta.Session.query(model.Composer).filter_by(firstname='Sergio').one() )
    p.works.append(work)
    meta.Session.add(p)

    # ---


    work = model.Work()
    work.title = 'Digital Animation 1'
    work.blurb = 'For two pianos'
    work.description = 'Each order is for one booklet only. Two are needed to play the duet.'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1001'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Toccata 1'
    work.blurb = 'For Piano 4 hands'
    work.description = 'Each order is for one booklet only. Two are needed to play the duet.'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1002'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Five Abstract Pieces for Two Pianos'
    work.description = 'Each order is for one booklet only. Two are needed to play the duet.'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1003'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Ballade for Two Pianos'
    work.description = 'Each order is for one booklet only. Two are needed to play the duet.'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1004'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Dancing Princess'
    work.blurb = 'For students'
    work.price = 5
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.description = 'Playfully'
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1005'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'The Unicorn Ride'
    work.blurb = 'For students'
    work.price = 5
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1006'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'For Children at Heart'
    work.blurb = 'For students'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1007'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Weekend'
    work.blurb = 'For students'
    work.price = 5
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1008'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Ten Preludes'
    work.blurb = 'For students'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1009'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'A Family of Lanipero'
    work.blurb = 'For students'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1010'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Canzicranz Dance'
    work.price = 5
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    c = model.Soundclip()
    c.path = '/music/michael/Canzicranz_Dance.mp3'
    work.soundclips.append( c )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1011'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Sprites'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1012'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Nocturne'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    c = model.Soundclip()
    c.path = '/music/michael/Nocturne_2.mp3'
    work.soundclips.append( c )
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1013'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Berceuse'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.key = meta.Session.query(model.Key).filter_by(name='Atonal').one()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.description = "In 2000, the pianist Roberto Prosseda began performing Williams' Berceuse and other Chopin stylized music on concerts juxtaposed with Chopin"
    c = model.Soundclip()
    #c.path = '/music/Williams, Michael Glenn - track01.mp3'
    c.path = '/music/michael/Berceuse.mp3'
    work.soundclips.append( c )
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1014'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Ring Tones'
    work.price = 10
    work.blurb = 'for Solo Piano'
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.description = 'Inspired by cell phone ring tones'
    work.image = '/ringtones.jpg'
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    movement = model.Movement()
    movement.number = 1
    movement.title = str(movement.number)
    movement.description = 'Have fun with the bell sounds'
    movement.key = meta.Session.query(model.Key).filter_by(name='B flat major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 2
    movement.title = str(movement.number)
    movement.description = 'Allegro brilliante'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 3
    movement.title = str(movement.number)
    movement.description = 'Allegro'
    movement.key = meta.Session.query(model.Key).filter_by(name='E flat major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 4
    movement.title = str(movement.number)
    movement.description = 'Flowing, with energy'
    movement.key = meta.Session.query(model.Key).filter_by(name='F major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 5
    movement.title = str(movement.number)
    movement.description = 'With bounce'
    movement.key = meta.Session.query(model.Key).filter_by(name='E flat major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 6
    movement.title = str(movement.number)
    movement.description = 'Have fun with the bell sounds'
    movement.key = meta.Session.query(model.Key).filter_by(name='B flat major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 7
    movement.title = str(movement.number)
    movement.description = 'Flowing, mysterious'
    movement.key = meta.Session.query(model.Key).filter_by(name='E major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 8
    movement.title = str(movement.number)
    movement.description = 'Peaceful, lyrical'
    movement.key = meta.Session.query(model.Key).filter_by(name='E flat major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 9
    movement.title = str(movement.number)
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 10
    movement.title = str(movement.number)
    movement.description = 'Rocking, lyrical'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 11
    movement.title = str(movement.number)
    movement.description = 'Sparkling, brilliant'
    movement.key = meta.Session.query(model.Key).filter_by(name='B flat major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 12
    movement.title = str(movement.number)
    movement.description = 'Rythmic, a bit like rock music'
    movement.key = meta.Session.query(model.Key).filter_by(name='C flat major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 13
    movement.title = str(movement.number)
    movement.description = 'Like clockwork'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 14
    movement.title = str(movement.number)
    movement.description = 'Echoing and floating'
    movement.key = meta.Session.query(model.Key).filter_by(name='E major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1015'
    p.featured = True
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Collage'
    work.price = 15
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    movement = model.Movement()
    movement.number = 1
    movement.title = str(movement.number)
    movement.description = 'physique'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/Physique.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 2
    movement.title = str(movement.number)
    movement.description = 'the cock and the swan'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/The_Cock_and_the_Swan.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 3
    movement.title = str(movement.number)
    movement.description = 'beautiful spanish dancer'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/Beautiful_Spanish_Dancer.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 4
    movement.title = str(movement.number)
    movement.description = 'lullaby'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/Lullaby.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 5
    movement.title = str(movement.number)
    movement.description = 'romance'
    movement.key = meta.Session.query(model.Key).filter_by(name='B flat major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/Romance.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 6
    movement.title = str(movement.number)
    movement.description = 'military fanfare'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/Military_Fanfare.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 7
    movement.title = str(movement.number)
    movement.description = 'brigades'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/Brigades.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 8
    movement.title = str(movement.number)
    movement.description = 'nocturne'
    movement.key = meta.Session.query(model.Key).filter_by(name='B flat major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Collage_Suite/Nocturne.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)


    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1016'
    #p.featured = True
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Moments'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    c = model.Soundclip()
    c.path = '/blah3.mp3'
    work.soundclips.append( c )
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    movement = model.Movement()
    movement.number = 1
    movement.title = str(movement.number)
    movement.description = 'Festive'
    movement.key = meta.Session.query(model.Key).filter_by(name='E major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 2
    movement.title = str(movement.number)
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 3
    movement.title = str(movement.number)
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 4
    movement.title = str(movement.number)
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 5
    movement.title = str(movement.number)
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    meta.Session.add(work)


    p = model.Publication()
    p.catalog_number = 'GW-MW01-1017'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)



    # ---
    work = model.Work()
    work.title = 'Tone Poems'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    movement = model.Movement()
    movement.number = 1
    movement.title = str(movement.number)
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 2
    movement.title = str(movement.number)
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 3
    movement.title = str(movement.number)
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 4
    movement.title = str(movement.number)
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 5
    movement.title = str(movement.number)
    movement.workid = work.id
    meta.Session.add(movement)

    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1018'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Songs Without Words'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    movement = model.Movement()
    movement.number = 1
    movement.title = str(movement.number)
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/michael/Songs_Without_Words_1.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 2
    movement.title = str(movement.number)
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/michael/Songs_Without_Words_2.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 3
    movement.title = str(movement.number)
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/michael/Songs_Without_Words_3.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1019'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)



    # ---
    work = model.Work()
    work.title = 'The Enchanted Forest'
    work.price = 15
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    movement = model.Movement()
    movement.number = 1
    movement.title = 'March of the Giant Bears'
    movement.description = 'With a heavy bounce'
    movement.key = meta.Session.query(model.Key).filter_by(name='E major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Enchanted_Forest/March_of_the_Giant_Bears.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 2
    movement.title = 'Enchanted Water'
    movement.description = 'water flowing uphill'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Enchanted_Forest/Enchanted_Water.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 3
    movement.title = 'Moonlight Nocturne'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Enchanted_Forest/Moonlight_Nocturne.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 4
    movement.title = 'Dance of the Wood Nymphs'
    movement.description = 'with a graceful sway'
    movement.key = meta.Session.query(model.Key).filter_by(name='E major').one()
    movement.workid = work.id
    c = model.Soundclip()
    c.path = '/music/Enchanted_Forest/Dance_of_the_Wood_Nymphs.mp3'
    movement.soundclips.append( c )
    meta.Session.add(movement)

    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1020'
    p.featured = True
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Suite for Piano'
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    movement = model.Movement()
    movement.number = 1
    movement.title = 'Entrance'
    movement.description = 'With bravura'
    movement.key = meta.Session.query(model.Key).filter_by(name='E major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 2
    movement.title = 'Short Theme and Variations'
    movement.description = 'Theme (right hand as if overtones)'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 3
    movement.title = 'Echoes'
    movement.description = 'Warm, intimate, blurred'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    movement = model.Movement()
    movement.number = 4
    movement.title = 'Nocturne'
    movement.description = 'Delicate'
    movement.key = meta.Session.query(model.Key).filter_by(name='C major').one()
    movement.workid = work.id
    meta.Session.add(movement)

    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1021'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # these two are unused
    # ---
    if 0:
        pub = model.Publication()
        pub.title = 'Nocturne (Fugit Amor)'
        pub.description = 'From Suite for Piano'

        meta.Session.add(pub)

        # ---
        pub = model.Publication()
        pub.title = 'Entrance'
        pub.description = 'From Suite for Piano'

        meta.Session.add(pub)

    # ---
    work = model.Work()
    work.title = 'Scherzo'
    work.pages = 12
    work.price = 5
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1022'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Anger Burst'
    work.pages = 5
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    piano = meta.Session.query(model.Instrument).filter_by(name='Piano').one()
    work.instruments.append( piano )

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1023'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Trio Populaire'
    work.price = 20
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    paths = ['/music/Williams - Trio Populaire - I. Fantastic Waltz.mp3',\
             '/music/Williams - Trio Populaire - II. Song Without Words.mp3',\
             '/music/Williams - Trio Populaire - III. Scherzo.mp3']
    for name in ['Clarinet','Piano','Cello']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    for n in range(1,3+1):
        c = model.Soundclip()
        c.path = paths[n-1]
        movement.soundclips.append( c )
        movement = model.Movement()
        movement.title = 'Movement %i'%n
        movement.number = n
        movement.workid = work.id
        meta.Session.add(movement)
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1024'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Collage Trio'
    work.price = 20
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    for name in ['Clarinet','Piano','Violin']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1025'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Sad, Lovely and Melancholy Airs for Flute and Piano'
    work.price = 10
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    for name in ['Flute','Piano']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1026'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Be Still as You Are Beautiful'
    work.price = 5
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Vocal').one() )
    for name in ['Tenor','Piano','Voice']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1027'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = "The Lord's Prayer"
    work.price = 5
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Vocal').one() )
    for name in ['Soprano','Tenor','Piano','Voice']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1028'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Three Little Pieces for String Quartet'
    work.price = 20
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    for name in ['Violin','Viola','Cello']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1029'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Music for Horn and Strings'
    work.price = 20
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    for name in ['French horn','Viola','Cello','Violin']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1030'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Music for Guitar and Strings'
    work.price = 20
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    for name in ['Guitar','Viola','Cello','Violin']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1031'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Open Music for Woodwind Quintet'
    work.price = 20
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    for name in ['Flute','Bassoon','Oboe','Clarinet','French horn']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1032'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Prelude for Violin and Piano'
    work.price = 10
    work.blurb = 'For students'
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    for name in ['Violin','Piano']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1033'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Fanfare and Postlude for Brass Choir'
    work.price = 20
    work.blurb = 'For students'
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Vocal').one() )
    for name in ['Voice']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1034'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'A Little Bit of Heaven for Male Quartet'
    work.price = 10
    work.blurb = 'For students'
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Vocal').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Arrangement').one() )
    for name in ['Voice']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1035'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Peter and the Wolf for Woodwind Quintet'
    work.price = 30
    work.blurb = 'For students'
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Chamber Music').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Arrangement').one() )
    for name in ['Flute','Bassoon','Oboe','Clarinet','French horn']:
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1036'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Tarantella (Italian Holiday) - Piano Solo'
    work.price = 10
    work.blurb = 'A tone poem for Piano and Orchestra'
    work.description = """
This piece for piano solo and orchestra was inspired both by the astonishing musicianship of Sean Chen, and by my visits to Italy in the last two years. I had the good fortune to holiday in Italy and tour Firenze, Roma, Venezia, Padova, Pisa, Latina, Bassiagno, etc with my esteemed friend Roberto Prosseda as guide. I met Nike Borghese, a last heir, who taught me about the Tears of San Lorenzo, and in her palace I improvised some themes used here. I also improvised on Franz Liszt's piano at the Ninfa Gardens, and tried to capture in this "musical fresco" some of the magic of that place as well. So this is a tone poem full of the color, bustle, humor and life, all the impressions of Italy made on my first visits.

It is my pleasure and honor to dedicate this work to "Sean Chen":http://seanchenpiano.com/. ("bio":http://chopin.org/Atimo_s/news/SeanChenBio.pdf) His love of all types of music, and his mastery of the most beautiful, directed my musical thought. His technical brilliance freed me from any concern over pianistic difficulty.

Michael Glenn Williams

Instrumentation:
2 Flutes (Piccolo)
2 Oboes
2 Clarinets in Bb
2 Bassoons
2 Horns in F
2 Trumpets in Bb
2 Trombones
1 Tuba
1 Timpani
1 Percussion (triangle, susp, cymbal, gong, piatti, tambourine)
1 Pitched percussion (campanelli, tubular bells, xylophone)
Piano Solo
Strings
    """
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    for name in 'Piano,Orchestra,Flute,Oboe,Clarinet,Bassoon,French horn,Trumpet,Trombone,Tuba,Timpani,Percussion,Violin,Viola,Cello,Double bass'.split(','):
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1037'
    p.featured = True
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)




    # ---
    work = model.Work()
    work.title = 'Tarantella (Italian Holiday) - Orchestral Reduction for Piano'
    work.price = 10
    work.blurb = 'A tone poem for Piano and Orchestra'
    work.description = """
This piece for piano solo and orchestra was inspired both by the astonishing musicianship of Sean Chen, and by my visits to Italy in the last two years. I had the good fortune to holiday in Italy and tour Firenze, Roma, Venezia, Padova, Pisa, Latina, Bassiagno, etc with my esteemed friend Roberto Prosseda as guide. I met Nike Borghese, a last heir, who taught me about the Tears of San Lorenzo, and in her palace I improvised some themes used here. I also improvised on Franz Liszt's piano at the Ninfa Gardens, and tried to capture in this "musical fresco" some of the magic of that place as well. So this is a tone poem full of the color, bustle, humor and life, all the impressions of Italy made on my first visits.

It is my pleasure and honor to dedicate this work to "Sean Chen":http://seanchenpiano.com/. ("bio":http://chopin.org/Atimo_s/news/SeanChenBio.pdf) His love of all types of music, and his mastery of the most beautiful, directed my musical thought. His technical brilliance freed me from any concern over pianistic difficulty.

Michael Glenn Williams

Instrumentation:
2 Flutes (Piccolo)
2 Oboes
2 Clarinets in Bb
2 Bassoons
2 Horns in F
2 Trumpets in Bb
2 Trombones
1 Tuba
1 Timpani
1 Percussion (triangle, susp, cymbal, gong, piatti, tambourine)
1 Pitched percussion (campanelli, tubular bells, xylophone)
Piano Solo
Strings
    """
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    for name in 'Piano,Orchestra,Flute,Oboe,Clarinet,Bassoon,French horn,Trumpet,Trombone,Tuba,Timpani,Percussion,Violin,Viola,Cello,Double bass'.split(','):
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1047'
    p.featured = False
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    # ---
    work = model.Work()
    work.title = 'Tarantella (Italian Holiday) - Orchestral Score'
    work.price = 30
    work.blurb = 'A tone poem for Piano and Orchestra'
    work.description = """
This piece for piano solo and orchestra was inspired both by the astonishing musicianship of Sean Chen, and by my visits to Italy in the last two years. I had the good fortune to holiday in Italy and tour Firenze, Roma, Venezia, Padova, Pisa, Latina, Bassiagno, etc with my esteemed friend Roberto Prosseda as guide. I met Nike Borghese, a last heir, who taught me about the Tears of San Lorenzo, and in her palace I improvised some themes used here. I also improvised on Franz Liszt's piano at the Ninfa Gardens, and tried to capture in this "musical fresco" some of the magic of that place as well. So this is a tone poem full of the color, bustle, humor and life, all the impressions of Italy made on my first visits.

It is my pleasure and honor to dedicate this work to "Sean Chen":http://seanchenpiano.com/. ("bio":http://chopin.org/Atimo_s/news/SeanChenBio.pdf) His love of all types of music, and his mastery of the most beautiful, directed my musical thought. His technical brilliance freed me from any concern over pianistic difficulty.

Michael Glenn Williams

Instrumentation:
2 Flutes (Piccolo)
2 Oboes
2 Clarinets in Bb
2 Bassoons
2 Horns in F
2 Trumpets in Bb
2 Trombones
1 Tuba
1 Timpani
1 Percussion (triangle, susp, cymbal, gong, piatti, tambourine)
1 Pitched percussion (campanelli, tubular bells, xylophone)
Piano Solo
Strings
    """
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    for name in 'Piano,Orchestra,Flute,Oboe,Clarinet,Bassoon,French horn,Trumpet,Trombone,Tuba,Timpani,Percussion,Violin,Viola,Cello,Double bass'.split(','):
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1048'
    p.featured = False
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    # ---
    work = model.Work()
    work.title = 'Tarantella (Italian Holiday) - Score and Parts'
    work.price = 100
    work.blurb = 'A tone poem for Piano and Orchestra'
    work.description = """
This piece for piano solo and orchestra was inspired both by the astonishing musicianship of Sean Chen, and by my visits to Italy in the last two years. I had the good fortune to holiday in Italy and tour Firenze, Roma, Venezia, Padova, Pisa, Latina, Bassiagno, etc with my esteemed friend Roberto Prosseda as guide. I met Nike Borghese, a last heir, who taught me about the Tears of San Lorenzo, and in her palace I improvised some themes used here. I also improvised on Franz Liszt's piano at the Ninfa Gardens, and tried to capture in this "musical fresco" some of the magic of that place as well. So this is a tone poem full of the color, bustle, humor and life, all the impressions of Italy made on my first visits.

It is my pleasure and honor to dedicate this work to "Sean Chen":http://seanchenpiano.com/. ("bio":http://chopin.org/Atimo_s/news/SeanChenBio.pdf) His love of all types of music, and his mastery of the most beautiful, directed my musical thought. His technical brilliance freed me from any concern over pianistic difficulty.

Michael Glenn Williams

Instrumentation:
2 Flutes (Piccolo)
2 Oboes
2 Clarinets in Bb
2 Bassoons
2 Horns in F
2 Trumpets in Bb
2 Trombones
1 Tuba
1 Timpani
1 Percussion (triangle, susp, cymbal, gong, piatti, tambourine)
1 Pitched percussion (campanelli, tubular bells, xylophone)
Piano Solo
Strings
    """
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Classical').one() )
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    for name in 'Piano,Orchestra,Flute,Oboe,Clarinet,Bassoon,French horn,Trumpet,Trombone,Tuba,Timpani,Percussion,Violin,Viola,Cello,Double bass'.split(','):
        instr = meta.Session.query(model.Instrument).filter_by(name=name).one()
        work.instruments.append( instr )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1049'
    p.featured = False
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    publication = model.Publication()
    publication.title = 'Chroma: New Music for Piano'
    publication.type = 'album'
    publication.catalog_number = 'GW-MM01-101'
    publication.price = 20
    publication.incomplete = True
    publication.featured = True
    publication.image = '/images/chroma.jpg'
    #publication.website = 'http://www.stradivarius.it/scheda.php?ID=801157033789400'
    publication.blurb = 'With Nocturne from Collage Suite'
    publication.composers.append(meta.Session.query(model.Composer).filter_by(firstname='Michael').one())
    publication.artists.append(meta.Session.query(model.Artist).filter_by(firstname='Jeri-Mae').one())
    publication.styles.append(meta.Session.query(model.Style).filter_by(name='Classical').one())
    publication.styles.append(meta.Session.query(model.Style).filter_by(name='Modern').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Piano').one())
    meta.Session.add(publication)

    work = meta.Session.query(model.Work).filter(model.Work.title == 'Collage').one()
    work.publications.append(publication)


    publication = model.Publication()
    publication.title = 'Digital Animation'
    publication.type = 'album'
    publication.catalog_number = 'GW-MW01-1050'
    publication.price = 20
    publication.incomplete = False
    publication.featured = True
    publication.image = '/images/digital_animation.jpg'
    publication.website = 'http://www.stradivarius.it/scheda.php?ID=801157033789400'
    publication.blurb = 'Digital Animation for Two Pianos by Michael Glenn Williams performed by Enrico Pompili & Gabriele Baldocci'
    publication.composers.append(meta.Session.query(model.Composer).filter_by(firstname='Michael').one())
    publication.artists.append(meta.Session.query(model.Artist).filter_by(firstname='Enrico').one())
    publication.artists.append(meta.Session.query(model.Artist).filter_by(firstname='Gabriele').one())
    publication.styles.append(meta.Session.query(model.Style).filter_by(name='Classical').one())
    publication.styles.append(meta.Session.query(model.Style).filter_by(name='Modern').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Piano').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Piano').one())
    meta.Session.add(publication)

    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Five Abstract Pieces')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Suite for Piano')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Scherzo')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Anger Burst')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Nocturne')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Canzicranz Dance')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Moments')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Tone Poems')).one()
    work.publications.append(publication)
    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Digital Animation')).one()
    work.publications.append(publication)


    publication = model.Publication()
    publication.title = 'Lyricism: Songs Without Words'
    publication.type = 'album'
    publication.catalog_number = 'GW-MW01-1038'
    publication.price = 20
    publication.incomplete = True
    publication.featured = True
    publication.image = '/images/lcover.gif'
    publication.website = 'http://www.aixrecords.com/catalog/michael_glenn_williams.html'
    #publication.website = 'http://www.aixrecords.com/cgi-bin/cgiwrap/aixrec/shop/detail.cgi?id=51'
    publication.blurb = 'Selected solo piano music of Michael Glenn Williams performed by Roberto Prosseda'
    publication.composers.append(meta.Session.query(model.Composer).filter_by(firstname='Michael').one())
    publication.artists.append(meta.Session.query(model.Artist).filter_by(firstname='Roberto').one())
    publication.styles.append(meta.Session.query(model.Style).filter_by(name='Classical').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Piano').one())
    meta.Session.add(publication)

    # attach works to publications...
    publication = meta.Session.query(model.Publication).filter(model.Publication.title.startswith('Lyricism')).one()

    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('The Enchanted')).one()
    work.publications.append(publication)

    work = meta.Session.query(model.Work).filter(model.Work.title =='Collage').one()
    work.publications.append(publication)

    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Berceuse')).one()
    work.publications.append(publication)

    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Songs Without')).one()
    work.publications.append(publication)

    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Canzicranz')).one()
    work.publications.append(publication)

    work = meta.Session.query(model.Work).filter(model.Work.title.startswith('Tone Poems')).one()
    work.publications.append(publication)



    publication = model.Publication()
    publication.title = '1 40 4 20: Wet'
    publication.type = 'album'
    publication.catalog_number = 'GW-MW01-1039'
    publication.website = 'http://pocketjazz.com/wet.html'
    publication.description = 'Second jazz publication'
    publication.composers.append(meta.Session.query(model.Composer).filter_by(firstname='Michael').one())
    publication.styles.append(meta.Session.query(model.Style).filter_by(name='Jazz').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Piano').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Saxophone').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Guitar').one())
    meta.Session.add(publication)

    publication = model.Publication()
    publication.title = '1 40 4 20: Jazz Trespassers'
    publication.type = 'album'
    publication.catalog_number = 'GW-MW01-1040'
    publication.website = 'http://pocketjazz.com/trespass.html'
    publication.description = 'First jazz publication'
    publication.composers.append(meta.Session.query(model.Composer).filter_by(firstname='Michael').one())
    publication.styles.append(meta.Session.query(model.Style).filter_by(name='Jazz').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Piano').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Saxophone').one())
    publication.instruments.append(meta.Session.query(model.Instrument).filter_by(name='Guitar').one())
    meta.Session.add(publication)

    #jazz
    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = 'Pocket Rocket'
    work.description = 'Collection of original jazz music'
    work.instruments.append( meta.Session.query(model.Instrument).filter_by(name='Piano').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Jazz').one() )
    meta.Session.add(work)

    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = 'Vocal Collection'
    work.description = 'Collection of original jazz vocal music'
    work.instruments.append( meta.Session.query(model.Instrument).filter_by(name='Voice').one() )
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Jazz').one() )
    meta.Session.add(work)


    #popular song
    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = 'Songs for Christian worship'
    work.description = 'Collection of 50 original songs for Christian worship'
    work.price = 20
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Popular Song').one() )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1041'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = "Chansons de l'amour perdu"
    work.description = "Collection of 30 original popular songs"
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Popular Song').one() )
    meta.Session.add(work)

    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = "I Like That About You (Wedding Song)"
    work.price = 10
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Popular Song').one() )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1042'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    #musical theater
    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = "Alexander's Very Bad Day"
    work.price = 30
    work.description = "Children's musical"
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Musical Theater').one() )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1043'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = "Commander Toad and the Space Pirates"
    work.price = 30
    work.description = "Children's musical"
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Musical Theater').one() )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1044'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = "The Name of the Tree"
    work.price = 30
    work.description = "Children's musical"
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Musical Theater').one() )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1045'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)


    work = model.Work()
    work.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    work.title = "Walk in faith"
    work.price = 30
    work.description = "Youth musical"
    work.styles.append( meta.Session.query(model.Style).filter_by(name='Musical Theater').one() )
    meta.Session.add(work)

    p = model.Publication()
    p.catalog_number = 'GW-MW01-1046'
    p.composers.append( work.composer )
    p.styles = work.styles
    p.instruments = work.instruments
    p.works.append(work)
    meta.Session.add(p)

    #film and television
    credit = model.Work()
    credit.title = 'King of the Hill'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Film').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)

    credit = model.Work()
    credit.title = 'The Limey'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Film').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)

    credit = model.Work()
    credit.title = 'The Critic'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Television').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)

    credit = model.Work()
    credit.title = 'Chicago Hope'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Television').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)

    credit = model.Work()
    credit.title = 'Wonderland'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Film').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)

    credit = model.Work()
    credit.title = 'Younger & Younger'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Film').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)

    credit = model.Work()
    credit.title = 'Wicker Park'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Film').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)

    credit = model.Work()
    credit.title = 'House of Yes'
    credit.styles.append( meta.Session.query(model.Style).filter_by(name='Film').one() )
    credit.composer = meta.Session.query(model.Composer).filter_by(firstname='Michael').one()
    meta.Session.add(credit)





    meta.Session.commit()
