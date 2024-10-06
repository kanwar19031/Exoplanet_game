import streamlit as st

def Exo():
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("https://cdn.esahubble.org/archives/images/screen/heic1619a.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.title("CHRONICLES OF EXOPLANET EXPLORATION")
    st.write("Here are some beautiful images related to exoplanets and astronomy:")

    # Adding full content and corresponding audio for each topic

    # What are exoplanets?
    st.header("What are exoplanets?")
    st.write("""
    Imagine peering beyond our solar system, what can one expect to discover? Billions of stars, galaxies, meteors and many other mesmerizing things but have you ever considered the possibility of celestial bodies like earth and other planets of our solar system orbiting distant stars? These very bodies are called exoplanets, the cosmic neighbors we’ve just begun to meet.
    Any planet that lies beyond the Kuiper belt is called an exoplanet. The majority of them revolve around other stars, but certain exoplanets, known as rogue planets, are free-floating and not connected to any star. Out of the billions of exoplanets that we think exist, we have confirmed more than 5,600. They come in a wide variety of sizes, from gas giants larger than Jupiter to small, rocky planets about as big around as Earth or Mars. On average, it is estimated that there is at least one planet for every star in the galaxy. That means there's something on the order of billions of planets in our galaxy alone, many in Earth's size range. They can be hot enough to boil metal or locked in deep freeze. They can orbit their stars so tightly that a “year” lasts only a few days; they can orbit two suns at once. Most of the exoplanets discovered so far are in a relatively small region of our galaxy, the Milky Way. ("Small" meaning within thousands of light-years of our solar system; one light-year equals 5.88 trillion miles or 9.46 trillion kilometers.) Even the closest known exoplanet to Earth, Proxima Centauri b, is still about 4 light-years away. We know there are more planets than stars in the galaxy.
    """)
    st.audio('Audio/introduction to exo planets.mp3')

    # History of exoplanet discovery
    st.header("History of exoplanet discovery")
    st.write("""
    Numerous planets have been discovered circling stars outside of our Solar System since the first exoplanet was discovered, which was a little over 20 years ago. Several of these newly discovered planets differ greatly from those that orbit our Sun, and even the architecture of exoplanetary systems is not at all like that of our own.  For some of these far-off worlds, astonishingly substantial data has come to light throughout time. But the question lies in how did we actually come across these exoplanets? Did the discovery naturally occur or was it the outcome of some theoretical research? Giordano Bruno was one of the first people to think that other stars might also have planets. This was way back in the 16th century. It was an idea that Isaac Newton agreed with. By the late 19th century, people were starting to claim they had found these so-called exoplanets. One of the first was the astronomer, William Stephen Jacob. He saw anomalies in the orbits of the stars in the 70 Ophiuchi binary system. He said these could be from a planet orbiting the system. More work by Thomas Jefferson Jackson See seemed to confirm what William thought. Thomas calculated there was a dark object orbiting the stars every 36 years. With better telescopes, we now know that this isn't true. The first exoplanet was discovered in 1992. In fact, the first discovery wasn't just 1 planet it was 2! Poltergeist and Phobetor were found orbiting a pulsar called PSR B1257+12. In 1994, a much smaller 3rd planet was found in the system, named Draugr. These new worlds opened up a new field of astronomy and were soon followed by other discoveries! The discovery was made in 1992 by Aleksander Wolszczan and Dale Frail, working at the Arecibo Observatory in Puerto Rico and the National Radio Astronomy Observatory in New Mexico, USA. They detected the tell-tale subtle changes to the timing of the pulsar's pulsed emission that indicated the presence of the planets.
    """)
    st.audio('Audio/history.mp3')

    # How do we find exoplanets?
    st.header("**How do we find exoplanets?**")
    st.write("""
    Finding exoplanets is like searching for a firefly next to the spotlight, these planets don’t give up their secrets easily but using precise measurements and advanced technology, we’ve devised methods to reveal these hidden cosmic travellers. There are five methods scientists commonly use to discover exoplanets. The two main techniques are the transit and radial velocity methods.
    """)
    st.audio('Audio/Detection 1st para.mp3')

    # Radial Velocity
    st.subheader("**Radial Velocity: Reading the Wobble**")
    st.write("""
    Stars wobble in space due to orbiting planets, which alters the hue of light that astronomers detect in stars. When viewed through a telescope, the gravitational pull of a star's revolving planets influences the star's visible spectrum. The spectrum will appear to have moved toward blue if it moves in the observer's direction. It will turn toward the red if it is traveling away from the observer. The radial velocity method is the technique by which this is observed. The planet discovered in 1995 was a hot, star-hugging gas giant believed to be about half the size of Jupiter. It tugged so hard on its parent star as it raced around in a four-day orbit that the star’s wobbling was obvious to earthly telescopes. Finding this fast-moving gas giant, known as 51 Pegasi b, kicked off what might be called the “classical” period of planet hunting. The early technique of tracking wobbling stars revealed one planet after another, many of them large “hot Jupiters” with tight, blistering orbits. The wobble method measures changes in a star’s “radial velocity.” The wavelengths of starlight are alternately squeezed and stretched as a star moves slightly closer, then slightly farther away from us. Approximately 500 planets have been discovered using this method.
    """)
    st.audio('Audio/Radial velocity.mp3')

    # Transit Method
    st.subheader("**Transits: Planets Found in Dips in Light**")
    st.write("""
    Most known exoplanets have been discovered using the transit method. A transit occurs when a planet passes between a star and its observer. Transits within our solar system can be observed from Earth when Venus or Mercury travel between us and the Sun. Transits reveal an exoplanet not by directly observing it from light-years away, but by detecting the slight dimming of its star as the planet passes in front. This dimming appears in light curves—graphs that display the star’s brightness over time. When the exoplanet crosses in front, the light curve shows a small dip in brightness. This data highlights the usefulness of transits: they allow us to determine various characteristics of exoplanets. By measuring the time it takes for the planet to complete one orbit (its period), we can calculate the size of its orbit. Additionally, the amount by which the star's brightness decreases helps us estimate the size of the planet itself. We can also learn about an exoplanet’s atmosphere during a transit. As it transits, some light will go through its atmosphere and that light can be analysed to determine what different atmospheric elements influenced its particular dispersion. Roughly 2,500 exoplanets have been found using this method.
    """)
    st.audio('Audio/Transit method.mp3')

    # Direct Imaging
    st.subheader("**Direct Imaging**")
    st.write("""
    Exoplanets are so faint and far away that they’re almost impossible to see, even with advanced telescopes. For this reason, most exoplanets discovered so far have been detected indirectly by the influence they exert on their host stars. However, recent technological advancements now enable astronomers to capture actual images and spectra of these distant worlds. The single pixels of light captured directly from exoplanets won't be enough to reveal surface features. But they will provide the next best thing: profiles of exoplanet atmospheres, and perhaps evidence of gases suggesting the presence of life. Planets can be billions of times dimmer than their host stars, so they’re usually lost in the glare. But by blocking the star’s light using a coronagraph or star shade, astronomers can image fainter planets in orbit. This technique works best for young, nearby planetary systems, whose planets are especially bright. Imaging Earth-like planets directly around Sun-like stars may be the most effective way to learn about the formation and evolution of our own solar system. Even more intriguingly, it might make countless additional worlds conceivably habitable visible to us.
    """)
    # You may add an audio file for Direct Imaging here if available
    # st.audio('Audio/Direct Imaging.mp3')

    # Gravitational Microlensing
    st.subheader("**Gravitational Microlensing**")
    st.write("""
    Gravitational lensing is an observational effect that occurs because the presence of mass warps the fabric of space-time, sort of like the dent a bowling ball makes when set on a trampoline. The impact is greatest in the vicinity of extremely enormous objects, such as whole galaxies and black holes. But even stars and planets cause a detectable degree of warping, called microlensing. Light travels in a straight line, but if space-time is bent – which happens near something massive, like a star – light follows the curve. Any time two stars align closely from our vantage point, light from the more distant star curves as it travels through the warped space-time around the nearer star. If the alignment is especially close, the nearer star acts like a natural cosmic lens, magnifying light from the background star creating a temporary spike in the brightness. That signal lets astronomers know there’s an intervening object, even if they can’t see it directly. Planets orbiting the lens star can produce a similar effect on a smaller scale. Microlensing is best suited to finding worlds from the habitable zone of their star and farther out. This includes ice giants, like Uranus and Neptune in our solar system, and even rogue planets — worlds freely roaming the galaxy unbound to any stars.
    """)
    st.audio('Audio/Gravitational microlensing.mp3')

    # Astrometry
    st.subheader("**Astrometry**")
    st.write("""
    Astrometry is the science (and art!) of precision measurement of stars' locations in the sky. When planet hunters use astrometry, they look for a minute but regular wobble in a star's position compared to the positions of other stars. If such a periodic shift is detected, it is almost certain that the star is being orbited by an unseen companion planet. Exoplanets and their stars pull on each other. We can’t see the exoplanet, but we can see the star move. The star’s motion compared to other stars shows that an exoplanet exists. Astrometry is one of the most precise methods for detecting extrasolar planets. Unlike transit photometry, it doesn't rely on the distant planet being perfectly aligned with Earth's line of sight, allowing it to be used on a much wider range of stars. Additionally, unlike the radial velocity method, astrometry offers a more accurate measurement of a planet's true mass, rather than just providing a minimum estimate. This makes it an invaluable tool for astronomers seeking detailed information about distant worlds.
    """)
    st.audio('Audio/Astrometry.mp3')

    st.title("**CHRONICLES OF EXOPLANET EXPLORATION**")
    st.write("Here are some beautiful images related to exoplanets and astronomy:")

    # Types of exoplanets
    st.header("**Types of exoplanets**")
    st.write("""
    Often, when we think of planets, we picture well-known worlds like Jupiter or Earth. However, there is a wide variety of exoplanets—some that are completely undiscovered. Exoplanet diversity shows how wild and varied the universe is, from cold super-Earths to blazing gas giants. Over the last three decades, we have discovered all kinds of strange planets we never knew existed and that have no analog in our solar system. Each planet type varies in interior and exterior depending on the composition.
    """)
    st.audio('Audio/Types of exoplanets intro.mp3')

    # Super-Earths
    st.subheader("**Super-Earths**")
    st.write("""
    Super-Earths, a class of planets not found in our solar system, are more massive than Earth but less massive than ice giants like Neptune and Uranus. They can be composed of gas, rock, or a mix of both, and typically range from twice Earth's size to up to 10 times its mass. It is a reference only to an exoplanet’s size – larger than Earth and smaller than Neptune – but not suggesting they are necessarily similar to our home planet. The true nature of these planets remains shrouded in uncertainty because we have nothing like them in our own solar system – and yet, they are common among planets found so far in our galaxy. We don’t yet know enough about these planets to tell at what point they might lose a rocky surface. Some interesting facts about super earths are:
    - These types of planets have temperatures hot enough to vaporise metals, called super-hot super-Earths.
    - Some of them have a star like our sun.
    - They might be found hiding at the edge of our solar system.
    """)
    st.audio('Audio/Super earth.mp3')

    # Case study of Super-Earth 55 Cancri e
    st.subheader("**Case study of climate of Super-Earth 55 Cancri e**")
    st.write("""
    Observations from NASA's Spitzer Space Telescope led to the first temperature map of a super-Earth in 2016. The map reveals extreme temperature swings from one side of the planet to the other, and hints at a reason for this: lava flows. At 41 light-years away, the warm super-Earth 55 Cancri e is comparatively close to Earth. Every eighteen hours, it whips around its star in a relatively tight orbit. Similar to how our Moon is to Earth, the planet is tidally locked by gravity due to its closeness to the star. This indicates that the night side of 55 Cancri is significantly colder and stays in the dark, while the day side is constantly cooking due to the star's immense heat. Using its infrared eyesight, Spitzer observed the planet for a total of eighty hours, witnessing it circle its star several times. These data allowed scientists to map temperature changes across the entire world. To their surprise, they found a dramatic temperature difference of 2,340 degrees Fahrenheit (1,300 Kelvin) from one side of the planet to the other. The hottest side is nearly 4,400 degrees Fahrenheit (2,700 Kelvin), and the coolest is 2,060 degrees Fahrenheit (1,400 Kelvin).
    """)
    st.audio('Audio/case study of super earth.mp3')

    # Neptunian planets
    st.subheader("**Neptunian planets**")
    st.write("""
    Neptunian exoplanets are similar in size to Neptune or Uranus in our solar system. (Neptune is about four times the size, or radius, of Earth and almost 17 times its mass.) Neptunian exoplanets may have a mixture of interiors, though all would be rocky with heavier metals at their cores. Neptunian planets typically have hydrogen- and helium-dominated atmospheres. We’re also discovering mini-Neptunes, planets smaller than Neptune and bigger than Earth. No planets like these exist in our solar system. Uranus and Neptune are primarily made up of hydrogen and helium, but they also contain water, ammonia, and methane. Because these substances are typically frozen in the cold outer regions of the solar system, the two planets are often called "ice giants"—though their interiors are warm enough that these "ices" are not actually frozen. The James Webb Space Telescope, launched in 2021, is getting our best looks yet at exoplanet atmospheres. Astronomers were elated to find clear skies on a Neptune-size planet called HAT-P-11b in 2017. Without clouds to block the view, they were able to identify water vapor molecules in the exoplanet's atmosphere. HAT-P-11b is gaseous with a rocky core, much like our own Neptune.
    """)
    st.audio('Audio/Neptunian.mp3')

    # Gas Giants
    st.subheader("**Gas Giants**")
    st.write("""
    A gas giant is a large planet mostly composed of helium and/or hydrogen. These planets, like Jupiter and Saturn in our solar system, don’t have hard surfaces and instead have swirling gases above a solid core. Gas giant exoplanets can be much larger than Jupiter, and much closer to their stars than anything found in our solar system. When gas giants are closer to their stars, they're called "hot Jupiters." There's more variety within these categories than it seems. For example, hot Jupiters were some of the first exoplanets discovered. They're like Jupiter, but they orbit so close to their stars that their temperatures reach thousands of degrees, making them extremely hot! The exoplanet HIP 67522 b, discovered in June 2020, is believed to be the youngest hot Jupiter ever found. It orbits a star around 17 million years old, while most hot Jupiters are more than a billion years old. Located about 490 light-years away, this planet is around 10 times bigger than Earth, nearly the size of Jupiter.
    """)
    st.audio('Audio/gas giants.mp3')

    # Case study of migrating gas giants
    st.subheader("**Case study of migrating gas giants and developing gas giants**")
    st.write("""
    There are three main hypotheses for how hot Jupiters get so close to their parent stars. One is that they simply form there and stay put. But it's hard to imagine planets forming in such an intense environment. Not only would the scorching heat vaporize most materials, but young stars frequently erupt with massive explosions and stellar winds, potentially dispersing emerging planets. It could be more likely that gas giants develop farther from their parent star, past a boundary called the snow line, where it's cool enough for ice and other solid materials to form. Jupiter-like planets are composed almost entirely of gas, but they contain solid cores. Gas giants could get their start in the gas-rich debris disk that surrounds a young star. A core produced by collisions among asteroids and comets provides a seed, and when this core reaches sufficient mass, its gravitational pull rapidly attracts gas from the disk to form the planet.
    """)
    st.audio('Audio/gas giants case study.mp3')

    # Terrestrial planets
    st.subheader("**Terrestrial planets**")
    st.write("""
    Terrestrial planets, which are Earth-sized or smaller, are rocky worlds made of materials like rock, silicate, water, or carbon. To figure out if these planets have atmospheres, oceans, or signs of habitability, scientists need to study them further. Larger terrestrial exoplanets, which are at least twice the mass of Earth, are called super-Earths. Terrestrial planets typically have a solid or liquid surface and a bulk composition primarily composed of rock or iron. Although these distant worlds might have gaseous atmospheres, that doesn't make them particularly unique. We've found rocky planets in Earth's size range, at the right distance from their parent stars to harbour liquid water (this is known as the habitable zone).
    """)
    #st.audio('Audio/terrestrial planets.mp3')

    # Case study of 55 Cancri e
    st.subheader("**55 Cancri e**")
    st.write("""
    55 Cancri e is a well-known super-hot world, covered in a global ocean of lava, and has sparkling skies. It is one of the Super Earths orbiting the sun-like star 55 Cancri. Located 41 light years away in the constellation Cancer, it has a mass eight times that of the Earth. Its orbital period is merely 0.7 days on Earth, indicating that it circles its star very quickly.
    """)
    st.audio('Audio/55 cancri e.mp3')




    # Notable exoplanets
    st.header("Some most notable exoplanets")
    
    # Kepler-16b
    st.subheader("Kepler-16b")
    st.write("""
    It is a giant planet composed mainly of gas. It was discovered in the year 2011 with the help of Kepler telescope. Its orbital period is 228.8 days and has a mass of 0.333 tomes the mass of Jupiter. It has a radius of 0.754 times Jupiter’s radius. Kepler-16b is a world where two suns set over the horizon instead of just one, the first Tatooine- like planet found in our galaxy. Tatooine is the name of Luke Skywalker’s home world in the science fiction movie Star Wars. This planet falls in the category of Gas Giants. In this case, the planet is not thought to be habitable. It is acold world with a gaseous surface but like Tatooine it circles two stars. The largest of the two stars, a K dwarf, is about 69 percent the mass of our sun and the smallest, a red dwarf, is about 20 percent the sun’s mass.
    """)
    #st.audio('audio/kepler_16b.mp3')

    # Kepler-22b
    st.subheader("Kepler-22b")
    st.write("""
    This planet is a potential rocky world, larger than earth. It has a radius of 2.1 times that of earth’s and mass equal to 9.1 earths. It falls under the category of super earth and has an orbital period of 289.9 days. A possible ocean world orbiting in the habitable zone—the region around a star where the temperature is right for liquid water, a requirement for life on Earth. Kepler-22b was the first exoplanet ever discovered lying inside its parent star’s habitable zone. It was discovered by the now-retired Kepler Space Telescope and, at the time. Kepler 22-b lies about 15% closer to its parent star than Earth does to the Sun, which would make it significantly hotter, were it not balanced out by the fact that host star Kepler-22 shines 25% less brightly than the Sun.  It is an exoplanet orbiting Kepler-22  a sun-like G5 star about 600 light years from Earth.
    """)
    #st.audio('audio/kepler_22b.mp3')

    # Kelt-9b
    st.subheader("Kelt-9b")
    st.write("""
    Discovered in 2017 by TESS mission, KELT-9b is so hot that the heat tears molecules apart on the dayside. It orbits its parent star  KELT-9b. It is the hottest gas giant planet discovered so far. This planet is estimated to be   2.8 times more massive than Jupiter, but only half as dense. Scientists would expect the planet to have a smaller radius, but the extreme radiation from its host star has caused the planet's atmosphere to puff up like a balloon. KELT-9b is a gas giant 2.8 times more massive than Jupiter, but only half as dense. Scientists would expect the planet to have a smaller radius, but the extreme radiation from its host star has caused the planet's atmosphere to puff up like a balloon. It is 670 light years away from the earth. It’s very close to the bright star Sadr at the centre of the Northern Cross in the constellation Cygnus, the Swan. 
    """)
    #st.audio('audio/kelt_9b.mp3')

    # WASP-12b
    st.subheader("WASP-12b")
    st.write("""
    Discovered in 2008 by NASA’s Spitzer Space Telescope, the doomed planet WASP-12b is a hot Jupiter that orbits so close to its parent star which is a yellow dwarf called WASP-12 , it's being torn apart. It takes this alien world only 1.1 days to completely circle its Sun. Its radius is 1.937 times of Jupiter and has a mass of 1.465 Jupiters.  The star's gravity also pulls material off the planet into a disk around the star. In 10 million years, this alien world could be completely consumed. WASP-12b is a scorching gas giant nearly twice the size of Jupiter, with temperatures reaching about 4,000 degrees Fahrenheit (2,210 degrees Celsius). Due to intense gravitational forces, the planet is being stretched by tidal forces, giving it an egg-like shape. It is located in the constellation Auriga which is 1,200 light years away. 
    """)
    #st.audio('audio/wasp_12b.mp3')

    # 55 Cancri e
    st.subheader("55 Cancri e")
    st.write("""
    This super-hot world is covered in a global ocean of lava and has sparkling skies. This planet is one of the Super Earths orbiting the sun 55 Cancri c . It is located 41 light years away in the constellation Cancer has a mass eight times that of the earth and is characterised by permanent day and night sides. Its orbital period is merely 0.7 days on earth. It is suggested that the planet may be surrounded by an atmosphere rich in carbon dioxide (CO2) or carbon monoxide (CO). Because it is so close to its star, the planet is extremely hot and is thought to be covered in molten rock. Researchers think that the gases that make up the atmosphere could have bubbled out of the magma. An atmosphere on this planet would likely be complex and quite variable due to interactions with the magma ocean. In addition to carbon monoxide or carbon dioxide, there could be gases like nitrogen, water vapor, sulphur dioxide, some vaporized rock, and even short-lived clouds made of tiny droplets of lava condensed from the air. It was discovered by Nasa’s Hubble space Telescope in the year 2004.
    """)
    #st.audio('audio/55_cancri_e.mp3')

    # Habitability and search for Life
    st.header("Habitability and search for Life")
    st.write("""
    This topic can be divided into 2 parts for easy understanding
    1.	Habitability   - 

    Habitability or habitable zone can be defined as where conditions might be just right – neither too hot nor too cold – for life. When looking for planets that might support life, scientists focus on ones that are similar to Earth. But what does "similar" really mean? Many rocky planets about the same size as Earth have been found, which is a good sign for life. On the other hand, big gas planets like Jupiter seem much less likely to support life, based on what we've seen in our solar system. However, most of the Earth-sized planets we've discovered are orbiting small, dim stars called red dwarfs. Finding Earth-sized planets around stars like our Sun is much harder. 

    Where Are We Searching for Life, and Why? 
    Scientists are looking for planets that have things in common with Earth, like their size, what they are made of, and whether they are in the “habitable zone”—the area around a star where it’s not too hot or too cold, so water could exist. Water is important because life on Earth needs it. By finding planets with these Earth-like features, scientists hope to discover places where life might be possible. We’re especially interested in Earth-sized planets because they are more likely to have a solid surface and the right atmosphere to support life. Planets orbiting stars similar to our Sun are ideal, but they are harder to detect due to their distance and the faintness of their signals. So far, most of the exoplanets we’ve found that might be habitable are orbiting red dwarf stars, which are smaller and cooler than the Sun.


    2.	The search for life

    Whether or not life exists beyond Earth is one of the biggest questions we’ve ever asked. Finding the answer would change the way we see the universe. If we discover lots of life out there, it would mean the universe is full of living things. If life is rare, it would show how special and delicate life is. And if we find no other life, it would mean we might be alone in the universe. In the coming years, we’ll get closer to finding a planet that looks like a twin of Earth. It would be a small, rocky planet with clouds, oceans, and an atmosphere that could show signs of life. This might include gases like oxygen, carbon dioxide, and methane. While each gas on its own might not mean much, when they’re found together, they could be a strong clue that life is possible there.

    """)
    #st.audio('audio/habitability_and_search_for_life.mp3')

    # NASA’s Search for Life
    st.subheader("NASA’s Search for Life")
    st.write("""
    NASA's main goal in its Exoplanet Program is to find clear signs of life on other planets. The atmospheres of exoplanets (planets outside our solar system) might contain clues that life exists there. To find these clues, scientists study the light that passes through a planet's atmosphere, using a method called transmission spectroscopy. This process is like reading a barcode. When light from a star goes through the planet's atmosphere, some parts of the light are absorbed, leaving dark gaps in the light spectrum. These gaps tell us what gases are in the atmosphere. For example, one set of gaps might show methane, another might show oxygen. If we see both together, it could mean that life is present. Or, we might see a pattern that shows pollution, like smog.

    Collaborators in the Quest

    NASA scientists searching for life beyond Earth work together with experts in different areas. Some study our solar system, while others focus on ancient or extreme life forms here on Earth, and even on the Sun. There could be signs of life on Mars, Jupiter’s moon Europa, or Saturn’s moon Enceladus, and future missions are being planned to explore these places. Studying how life started on Earth, or how extreme forms of life survive in harsh conditions, can help us look for life on other planets. To fully understand distant exoplanets, we also need to know more about the stars they orbit, and learning more about our Sun can help us understand other stars too.

    """)
    #st.audio('audio/nasa_search_for_life.mp3')

    # The technology behind exoplanet exploration
    st.header("The technology behind exoplanet exploration")
    st.write("""
    The technology behind exoplanet exploration

    Powerful telescopes are essential for looking at distant stars and their planets. Space telescopes, like the Hubble and James Webb Space Telescopes, can gather information without the interference of Earth’s atmosphere, allowing scientists to see faint light from faraway planets.

    1.	Space Telescopes-

        ●	Hubble Space Telescope-
    Launched in 1990, Hubble is one of the most well-known telescopes. It orbits Earth, avoiding atmospheric distortion. Hubble has made significant contributions to exoplanet research by using spectroscopy to analyse the light from stars and study the atmospheres of known exoplanets. This helps scientists identify the gases present in those atmospheres.

       ●	James Webb Space Telescope (JWST)
    Launched in 2021, JWST is designed to observe infrared light, allowing it to see objects that are too faint or cool for other telescopes. It will analyse exoplanet atmospheres for signs of habitability and potential life. It can detect water vapor, carbon dioxide, and other important gases by studying how they absorb and emit infrared light.

    2.	Ground Based Telescopes

        ●	Keck observatory
    Located in Hawaii, this observatory has two of the world’s largest optical telescopes equipped with adaptive optics. The Keck Observatory is used for detecting exoplanets primarily through the radial velocity method, which measures a star’s wobble caused by an orbiting planet’s gravity.

        ●	Very large Telescope (VLT)
    Situated in Chile, the VLT consists of four individual telescopes that can work together. The VLT enhances sensitivity and resolution, allowing astronomers to directly image exoplanets and conduct detailed studies of their atmospheres.

    3.	Transit Telescope

        ●	Kepler Space Telescope
    Launched in 2009, Kepler was specifically designed to find exoplanets using the transit method. Kepler monitored the brightness of thousands of stars. When a planet passes in front of its star (a transit), it causes a small dip in brightness. By analysing these dips, Kepler discovered thousands of exoplanets.

        ●	TESS (Transiting Exoplanet Survey Satellite)
    Launched in 2018, TESS focuses on nearby, bright stars. TESS looks for transits like Kepler but targets stars that are easier to observe from Earth. Its discoveries are intended to be followed up by other telescopes for detailed studies.

    4.	Direct Imaging Telescopes
        ●	SPHERE (Spectro-Polarimetric High-contrast Exoplanet Research)
    Installed on the VLT, SPHERE is specifically designed for direct imaging of exoplanets. SPHERE uses advanced techniques like coronagraphy, which blocks out the light from a star to reveal the planets around it. This allows scientists to study the planets’ atmospheres and surfaces.

        ●	GPI (Gemini Planet Imager)

    Located at the Gemini South Telescope in Chile, GPI is also focused on direct imaging of exoplanets. GPI uses adaptive optics and coronagraphy to capture clear images of exoplanets and analyse their atmospheres, searching for chemical signatures of potential life.

    5.	Future Telescopes

        ●	Nancy Grace Roman Space Telescope
    Planned for launch in the mid-2020s, this telescope will have a wide field of view. Roman will conduct surveys to find and study exoplanets using both transit and gravitational microlensing methods, allowing for the discovery of more planets.

        ●	Habitable Exoplanet Observatory (HabEx) and LUVOIR (Large UV/Optical/IR Surveyor)
    These are proposed future missions aimed at directly imaging Earth-like exoplanets. Both missions would study exoplanet atmospheres and search for signs of habitability. They are designed to block out starlight effectively, enabling clear views of nearby planets.

    """)
    #st.audio('audio/technology_behind_exoplanet_exploration.mp3')

    # Future of exoplanet exploration
    st.header("Future of exoplanet exploration")
    st.write("""
    The future of exploring planets outside our solar system (called exoplanets) is very exciting. With new technology and space missions, we will find and study more distant planets that might have the right conditions for life. There are some key areas we can focus on:
    1.	Better Ways to Find Planets

    New tools and stronger telescopes will help scientists discover smaller exoplanets, especially those similar to Earth and orbiting stars like our Sun. Future missions, like NASA’s James Webb Space Telescope, will improve our ability to find these planets and learn about their atmospheres.

    2.	Studying Atmospheres

    Scientists will analyse the atmospheres of exoplanets more thoroughly. By using special techniques, they can find out what gases are in the atmosphere, looking for signs of life like oxygen, methane, or water vapor.

    3.	Seeing planets directly

    New telescopes will allow us to take pictures of exoplanets directly, helping us see what their surfaces and atmospheres look like. For example, NASA’s Nancy Grace Roman Space Telescope will help us see planets better by blocking the bright light from their stars.

    4.	Exploring Habitable Zones-

    Scientists will keep looking at planets in the “habitable zone,” which is the area around a star where conditions might be just right for liquid water to exist. These areas are important because water is essential for life as we know it. Researchers will study planets around different types of stars, including our Sun and cooler stars like orange and red dwarfs, to find places that could support life.

    5.	Learning about exoplanet climates

    As we gather more information, we will learn about the climates of these planets. This knowledge will help us figure out which planets might be able to support life by studying things like clouds and weather patterns.

    6.	Future space probes

    In the distant future, we may be able to send small spacecraft to nearby exoplanets. Projects like Breakthrough Starshot   plan to send tiny, light-powered probes to explore other star systems. As we develop better technology, exploring exoplanets will help us answer the big question of whether there is life beyond Earth

    """)
    #st.audio('audio/future_of_exoplanet_exploration.mp3')

