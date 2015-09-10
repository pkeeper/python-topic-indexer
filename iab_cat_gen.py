from lxml import etree
s = """<table>
<tr><td>NEWS</td><td>National News</td></tr>
<tr><td>NEWS</td><td>Local News</td></tr>
<tr><td>NEWS</td><td>International News</td></tr>
<tr><td>LAW, GOVERNMENT &amp; POLITICS</td><td>Politics</td></tr>
<tr><td>LAW, GOVERNMENT &amp; POLITICS</td><td>Commentary</td></tr>
<tr><td>LAW, GOVERNMENT &amp; POLITICS</td><td>U.S. Government Resources</td></tr>
<tr><td>LAW, GOVERNMENT &amp; POLITICS</td><td>Legal Issues</td></tr>
<tr><td>LAW, GOVERNMENT &amp; POLITICS</td><td>Immigration</td></tr>
<tr><td>SPORTS</td><td>Football</td></tr>
<tr><td>SPORTS</td><td>Pro Basketball</td></tr>
<tr><td>SPORTS</td><td>Volleyball</td></tr>
<tr><td>SPORTS</td><td>Tennis</td></tr>
<tr><td>SPORTS</td><td>Table Tennis/Ping-Pong</td></tr>
<tr><td>SPORTS</td><td>Swimming</td></tr>
<tr><td>SPORTS</td><td>Olympics</td></tr>
<tr><td>SPORTS</td><td>Auto Racing</td></tr>
<tr><td>SPORTS</td><td>Bicycling</td></tr>
<tr><td>SPORTS</td><td>Bodybuilding</td></tr>
<tr><td>SPORTS</td><td>Horse Racing</td></tr>
<tr><td>SPORTS</td><td>Horses</td></tr>
<tr><td>SPORTS</td><td>Martial Arts</td></tr>
<tr><td>SPORTS</td><td>Power &amp; Motorcycles</td></tr>
<tr><td>SPORTS</td><td>Walking</td></tr>
<tr><td>SPORTS</td><td>Running/Jogging</td></tr>
<tr><td>SPORTS</td><td>Paintball</td></tr>
<tr><td>SPORTS</td><td>Hunting/Shooting</td></tr>
<tr><td>SPORTS</td><td>Golf</td></tr>
<tr><td>SPORTS</td><td>Game &amp; Fish</td></tr>
<tr><td>SPORTS</td><td>Fly Fishing</td></tr>
<tr><td>SPORTS</td><td>Scuba Diving</td></tr>
<tr><td>SPORTS</td><td>Sailing</td></tr>
<tr><td>SPORTS</td><td>Boxing</td></tr>
<tr><td>SPORTS</td><td>Climbing</td></tr>
<tr><td>SPORTS</td><td>Canoeing/Kayaking</td></tr>
<tr><td>SPORTS</td><td>Skateboarding</td></tr>
<tr><td>SPORTS</td><td>Skiing</td></tr>
<tr><td>SPORTS</td><td>Snowboarding</td></tr>
<tr><td>SPORTS</td><td>Surfing/Bodyboarding</td></tr>
<tr><td>SPORTS</td><td>World Soccer</td></tr>
<tr><td>SPORTS</td><td>Mountain Biking</td></tr>
<tr><td>SPORTS</td><td>Freshwater Fishing</td></tr>
<tr><td>SPORTS</td><td>Saltwater Fishing</td></tr>
<tr><td>SPORTS</td><td>Pro Ice Hockey</td></tr>
<tr><td>SPORTS</td><td>Baseball</td></tr>
<tr><td>SPORTS</td><td>Cheerleading</td></tr>
<tr><td>SPORTS</td><td>Cricket</td></tr>
<tr><td>SPORTS</td><td>Figure Skating</td></tr>
<tr><td>SPORTS</td><td>Inline Skating</td></tr>
<tr><td>SPORTS</td><td>NASCAR Racing</td></tr>
<tr><td>SPORTS</td><td>Rodeo</td></tr>
<tr><td>SPORTS</td><td>Rugby</td></tr>
<tr><td>SPORTS</td><td>Waterski/Wakeboard</td></tr>
<tr><td>ARTS &amp; ENTERTAINMENT</td><td>Television</td></tr>
<tr><td>ARTS &amp; ENTERTAINMENT</td><td>Movies</td></tr>
<tr><td>ARTS &amp; ENTERTAINMENT</td><td>Music</td></tr>
<tr><td>ARTS &amp; ENTERTAINMENT</td><td>Humor</td></tr>
<tr><td>ARTS &amp; ENTERTAINMENT</td><td>Books &amp; Literature</td></tr>
<tr><td>ARTS &amp; ENTERTAINMENT</td><td>Fine Art</td></tr>
<tr><td>ARTS &amp; ENTERTAINMENT</td><td>Celebrity Fan/Gossip</td></tr>
<tr><td>EDUCATION</td><td>English as a 2nd Language</td></tr>
<tr><td>EDUCATION</td><td>Language Learning</td></tr>
<tr><td>EDUCATION</td><td>7-12 Education</td></tr>
<tr><td>EDUCATION</td><td>K-6 Educators</td></tr>
<tr><td>EDUCATION</td><td>College Life</td></tr>
<tr><td>EDUCATION</td><td>Graduate School</td></tr>
<tr><td>EDUCATION</td><td>Homework/Study Tips</td></tr>
<tr><td>EDUCATION</td><td>Adult Education</td></tr>
<tr><td>EDUCATION</td><td>Private School</td></tr>
<tr><td>EDUCATION</td><td>Special Education</td></tr>
<tr><td>EDUCATION</td><td>Distance Learning</td></tr>
<tr><td>EDUCATION</td><td>College Administration</td></tr>
<tr><td>EDUCATION</td><td>Homeschooling</td></tr>
<tr><td>EDUCATION</td><td>Art History</td></tr>
<tr><td>EDUCATION</td><td>Studying Business</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Dining Out</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>American Cuisine</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Coffee/Tea</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Desserts &amp; Baking</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Health/Lowfat Cooking</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Barbecues &amp; Grilling</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Cocktails/Beer</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Vegetarian</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Cuisine-Specific</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Chinese Cuisine</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>French Cuisine</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Wine</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Food Allergies</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Italian Cuisine</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Mexican Cuisine</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Japanese Cuisine</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Vegan</td></tr>
<tr><td>FOOD &amp; DRINK</td><td>Cajun/Creole</td></tr>
<tr><td>SOCIETY</td><td>Marriage</td></tr>
<tr><td>SOCIETY</td><td>Dating</td></tr>
<tr><td>SOCIETY</td><td>Ethnic Specific</td></tr>
<tr><td>SOCIETY</td><td>Weddings</td></tr>
<tr><td>SOCIETY</td><td>Divorce Support</td></tr>
<tr><td>SOCIETY</td><td>Senior Living</td></tr>
<tr><td>SOCIETY</td><td>Teens</td></tr>
<tr><td>SOCIETY</td><td>Gay Life</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Nutrition</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Weight Loss</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Exercise</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Sexuality</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Women's Health</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Men's Health</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Infertility</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Cholesterol</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Heart Disease</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Headaches/Migraines</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Cancer</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Brain Tumor</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>GERD/Acid Reflux</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Chronic Fatigue Syndrome</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Chronic Pain</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Allergies</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Cold &amp; Flu</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Dental Care</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Depression</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Psychology/Psychiatry</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>A.D.D.</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Panic/Anxiety Disorders</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Pediatrics</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Physical Therapy</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Orthopedics</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Smoking Cessation</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Substance Abuse</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Sleep Disorders</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Diabetes</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Dermatology</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Epilepsy</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Autism/PDD</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Asthma</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Alternative Medicine</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Herbs for Health</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Senior Health</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Thyroid Disease</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Incontinence</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>IBS/Crohn's Disease</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Deafness</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Holistic Healing</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Incest/Abuse Support</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Bipolar Disorder</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>AIDS/HIV</td></tr>
<tr><td>HEALTH &amp; FITNESS</td><td>Arthritis</td></tr>
<tr><td>STYLE &amp; FASHION</td><td>Fashion</td></tr>
<tr><td>STYLE &amp; FASHION</td><td>Clothing</td></tr>
<tr><td>STYLE &amp; FASHION</td><td>Beauty</td></tr>
<tr><td>STYLE &amp; FASHION</td><td>Accessories</td></tr>
<tr><td>STYLE &amp; FASHION</td><td>Jewelry</td></tr>
<tr><td>STYLE &amp; FASHION</td><td>Body Art</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Financial News</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Beginning Investing</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Investing</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Insurance</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Credit/Debt &amp; Loans</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Retirement Planning</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Stocks</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Tax Planning</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Mutual Funds</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Financial Planning</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Hedge Fund</td></tr>
<tr><td>PERSONAL FINANCE</td><td>Options</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Pregnancy</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Parenting - K-6 Kids</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Babies &amp; Toddlers</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Daycare/Pre School</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Family Internet</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Parenting teens</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Eldercare</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Adoption</td></tr>
<tr><td>FAMILY &amp; PARENTING</td><td>Special Needs Kids</td></tr>
<tr><td>SHOPPING</td><td>Comparison Engines</td></tr>
<tr><td>SHOPPING</td><td>Couponing</td></tr>
<tr><td>SHOPPING</td><td>Contests &amp; Freebies</td></tr>
<tr><td>REAL ESTATE</td><td>Buying/Selling Homes</td></tr>
<tr><td>REAL ESTATE</td><td>Apartments</td></tr>
<tr><td>REAL ESTATE</td><td>Architects</td></tr>
<tr><td>AUTOMOTIVE</td><td>Buying/Selling Cars</td></tr>
<tr><td>AUTOMOTIVE</td><td>Motorcycles</td></tr>
<tr><td>AUTOMOTIVE</td><td>Car Culture</td></tr>
<tr><td>AUTOMOTIVE</td><td>Certified Pre-Owned</td></tr>
<tr><td>AUTOMOTIVE</td><td>Auto Repair</td></tr>
<tr><td>AUTOMOTIVE</td><td>Auto Parts</td></tr>
<tr><td>AUTOMOTIVE</td><td>Road-Side Assistance</td></tr>
<tr><td>AUTOMOTIVE</td><td>Vintage Cars</td></tr>
<tr><td>AUTOMOTIVE</td><td>Diesel</td></tr>
<tr><td>AUTOMOTIVE</td><td>Wagon</td></tr>
<tr><td>AUTOMOTIVE</td><td>Sedan</td></tr>
<tr><td>AUTOMOTIVE</td><td>Luxury</td></tr>
<tr><td>AUTOMOTIVE</td><td>Hatchback</td></tr>
<tr><td>AUTOMOTIVE</td><td>Convertible</td></tr>
<tr><td>AUTOMOTIVE</td><td>Coupe</td></tr>
<tr><td>AUTOMOTIVE</td><td>Crossover</td></tr>
<tr><td>AUTOMOTIVE</td><td>Electric Vehicle</td></tr>
<tr><td>AUTOMOTIVE</td><td>Hybrid</td></tr>
<tr><td>AUTOMOTIVE</td><td>MiniVan</td></tr>
<tr><td>AUTOMOTIVE</td><td>Off-Road Vehicles</td></tr>
<tr><td>AUTOMOTIVE</td><td>Performance Vehicles</td></tr>
<tr><td>AUTOMOTIVE</td><td>Pickup</td></tr>
<tr><td>AUTOMOTIVE</td><td>Trucks &amp; Accessories</td></tr>
<tr><td>BUSINESS</td><td>Government</td></tr>
<tr><td>BUSINESS</td><td>Construction</td></tr>
<tr><td>BUSINESS</td><td>Advertising</td></tr>
<tr><td>BUSINESS</td><td>Marketing</td></tr>
<tr><td>BUSINESS</td><td>Human Resources</td></tr>
<tr><td>BUSINESS</td><td>Business Software</td></tr>
<tr><td>BUSINESS</td><td>Logistics</td></tr>
<tr><td>BUSINESS</td><td>Metals</td></tr>
<tr><td>BUSINESS</td><td>Biotech/Biomedical</td></tr>
<tr><td>BUSINESS</td><td>Agriculture</td></tr>
<tr><td>BUSINESS</td><td>Forestry</td></tr>
<tr><td>BUSINESS</td><td>Green Solutions</td></tr>
<tr><td>CAREERS</td><td>Job Search</td></tr>
<tr><td>CAREERS</td><td>College</td></tr>
<tr><td>CAREERS</td><td>Career Advice</td></tr>
<tr><td>CAREERS</td><td>Scholarships</td></tr>
<tr><td>CAREERS</td><td>Job Fairs</td></tr>
<tr><td>CAREERS</td><td>Resume Writing/Advice</td></tr>
<tr><td>CAREERS</td><td>Career Planning</td></tr>
<tr><td>CAREERS</td><td>Financial Aid</td></tr>
<tr><td>CAREERS</td><td>Telecommuting</td></tr>
<tr><td>CAREERS</td><td>Nursing</td></tr>
<tr><td>CAREERS</td><td>U.S. Military</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Interior Decorating</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Appliances</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Home Repair</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Remodeling &amp; Construction</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Landscaping</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Gardening</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Entertaining</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Home Theater</td></tr>
<tr><td>HOME &amp; GARDEN</td><td>Environmental Safety</td></tr>
<tr><td>TRAVEL</td><td>Hotels</td></tr>
<tr><td>TRAVEL</td><td>Honeymoons/Getaways</td></tr>
<tr><td>TRAVEL</td><td>Budget Travel</td></tr>
<tr><td>TRAVEL</td><td>Business Travel</td></tr>
<tr><td>TRAVEL</td><td>Air Travel</td></tr>
<tr><td>TRAVEL</td><td>Adventure Travel</td></tr>
<tr><td>TRAVEL</td><td>By US Locale</td></tr>
<tr><td>TRAVEL</td><td>Camping</td></tr>
<tr><td>TRAVEL</td><td>Cruises</td></tr>
<tr><td>TRAVEL</td><td>Spas</td></tr>
<tr><td>TRAVEL</td><td>Bed &amp; Breakfasts</td></tr>
<tr><td>TRAVEL</td><td>Europe</td></tr>
<tr><td>TRAVEL</td><td>South America</td></tr>
<tr><td>TRAVEL</td><td>United Kingdom</td></tr>
<tr><td>TRAVEL</td><td>Mexico &amp; Central America</td></tr>
<tr><td>TRAVEL</td><td>Japan</td></tr>
<tr><td>TRAVEL</td><td>Italy</td></tr>
<tr><td>TRAVEL</td><td>Greece</td></tr>
<tr><td>TRAVEL</td><td>France</td></tr>
<tr><td>TRAVEL</td><td>Eastern Europe</td></tr>
<tr><td>TRAVEL</td><td>Caribbean</td></tr>
<tr><td>TRAVEL</td><td>Canada</td></tr>
<tr><td>TRAVEL</td><td>Australia &amp; New Zealand</td></tr>
<tr><td>TRAVEL</td><td>Africa</td></tr>
<tr><td>TRAVEL</td><td>Traveling with Kids</td></tr>
<tr><td>TRAVEL</td><td>National Parks</td></tr>
<tr><td>TRAVEL</td><td>Theme Parks</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Cell Phones</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Cameras &amp; Camcorders</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Shareware/Freeware</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Entertainment</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Computer Reviews</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Home Video/DVD</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Antivirus Software</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>MP3/MIDI</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Net for Beginners</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Web Design/HTML</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>PC Support</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Web Search</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Windows</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>C/C++</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Unix</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Databases</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Internet Technology</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Java</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>JavaScript</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Linux</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Mac Support</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Portable</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Email</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Animation</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Computer Networking</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Computer Peripherals</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Data Centers</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Desktop Publishing</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Desktop Video</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Mac OS</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Net Conferencing</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Network Security</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Palmtops/PDAs</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Visual Basic</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Web Clip Art</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Graphics Software</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>Computer Certification</td></tr>
<tr><td>TECHNOLOGY &amp; COMPUTING</td><td>3-D Graphics</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Chess</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Guitar</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Board Games/Puzzles</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Photography</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Video &amp; Computer Games</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Jewelry Making</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Needlework</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Drawing/Sketching</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Arts &amp; Crafts</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Collecting</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Comic Books</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Card Games</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Birdwatching</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Painting</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Radio</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Sci-Fi &amp; Fantasy</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Home Recording</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Getting Published</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Beadwork</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Magic &amp; Illusion</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Roleplaying Games</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Stamps &amp; Coins</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Woodworking</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Screenwriting</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Scrapbooking</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Investors &amp; Patents</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Art/Technology</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Candle &amp; Soap Making</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Cigars</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Genealogy</td></tr>
<tr><td>HOBBIES &amp; INTERESTS</td><td>Freelance Writing</td></tr>
<tr><td>PETS</td><td>Cats</td></tr>
<tr><td>PETS</td><td>Dogs</td></tr>
<tr><td>PETS</td><td>Birds</td></tr>
<tr><td>PETS</td><td>Aquariums</td></tr>
<tr><td>PETS</td><td>Reptiles</td></tr>
<tr><td>PETS</td><td>Veterinary Medicine</td></tr>
<tr><td>PETS</td><td>Large Animals</td></tr>
<tr><td>SCIENCE</td><td>Weather</td></tr>
<tr><td>SCIENCE</td><td>Astrology</td></tr>
<tr><td>SCIENCE</td><td>Paranormal Phenomena</td></tr>
<tr><td>SCIENCE</td><td>Physics</td></tr>
<tr><td>SCIENCE</td><td>Biology</td></tr>
<tr><td>SCIENCE</td><td>Chemistry</td></tr>
<tr><td>SCIENCE</td><td>Space/Astronomy</td></tr>
<tr><td>SCIENCE</td><td>Geography</td></tr>
<tr><td>SCIENCE</td><td>Botany</td></tr>
<tr><td>SCIENCE</td><td>Geology</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Islam</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Atheism/Agnosticism</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Alternative Religions</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Christianity</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Judaism</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Buddhism</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Hinduism</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Catholicism</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Pagan/Wiccan</td></tr>
<tr><td>RELIGION &amp; SPIRITUALITY</td><td>Latter-Day Saints</td></tr>
<tr><td>UNCATEGORIZED</td><td>Social Media</td></tr>
</table>
"""
table = etree.XML(s)
rows = iter(table)
categories = []
for row in rows:
    values = ([col.text for col in row])
    values[0] = values[0].title()
    categories.append(values[::-1])
tier2 = dict(categories)
tier1 = set(tier2.values())
print repr(tier2)
print repr(tier1)
