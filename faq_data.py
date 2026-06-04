faq_categories = {
    "🎓 College FAQs": {
        "When does college reopen?": "Please check the latest academic calendar on the college website or contact the administration office for the most up-to-date information.",
        "What is the college timing?": "General college hours are 9:00 AM to 4:30 PM, Monday to Saturday. Specific department timings may vary.",
        "How do I get my hall ticket?": "You can download your hall ticket from the official student portal. Log in with your roll number and date of birth.",
        "Who is the HOD?": "Please contact the department office directly for the current Head of Department information.",
        "How do I get a bonafide certificate?": "Submit a written request to the college office or apply through the student portal. It typically takes 2–3 working days.",
        "What documents are needed for admission?": "You'll need 10th and 12th mark sheets, transfer certificate, community certificate, passport-size photos, and Aadhaar card.",
    },
    "💸 Scholarship FAQs": {
        "How to apply for a scholarship?": "Visit the scholarship section of the college website. You can also apply via the Tamil Nadu government scholarship portal at www.scholarships.gov.in.",
        "What scholarships are available?": "Scholarships include SC/ST scholarships, BC/MBC scholarships, merit-based scholarships, and central government scholarships like NSP.",
        "When is the scholarship deadline?": "Scholarship deadlines vary each year. Typically, applications open in August–September. Check the notice board or college website regularly.",
        "What is the income limit for scholarship elig": "For most government scholarships, the family annual income limit is ₹2.5 lakhs. Some scholarships allow up to ₹5 lakhs.",
    },
    "💼 Placement FAQs": {
        "What are placement opportunities?": "Placement opportunities depend on your academic performance, communication skills, and company requirements. Top recruiters visit campus annually.",
        "What is the average placement package?": "The average package ranges from ₹3–6 LPA depending on the company and branch. Some top companies offer up to ₹12 LPA.",
        "How do I register for placements?": "Register with the Training & Placement Cell at the beginning of your final year. Keep your resume updated on the placement portal.",
        "Which companies visit for campus recruitment?": "Companies like TCS, Infosys, Wipro, Cognizant, HCL, and several core engineering firms visit campus each year.",
        "Is there training provided before placements?": "Yes, the college provides aptitude training, soft skills workshops, and mock interviews through the T&P Cell.",
    },
    "🤖 AI FAQs": {
        "What is AI?": "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems, including learning, reasoning, and self-correction.",
        "What is Machine Learning?": "Machine Learning (ML) is a branch of AI that gives systems the ability to automatically learn and improve from experience without being explicitly programmed.",
        "What is Deep Learning?": "Deep Learning is a subset of Machine Learning using neural networks with many layers to learn representations of data with multiple levels of abstraction.",
        "What is Natural Language Processing?": "NLP is a field of AI that gives computers the ability to understand, interpret, and generate human language in a meaningful way.",
        "What is ChatGPT?": "ChatGPT is an advanced AI chatbot developed by OpenAI, based on the GPT (Generative Pre-trained Transformer) architecture. It can hold conversations, write code, and answer questions.",
        "What is Generative AI?": "Generative AI refers to AI systems that can generate new content — including text, images, audio, and video — based on patterns learned from training data.",
        "What is a neural network?": "A neural network is a series of algorithms modeled loosely after the human brain that recognizes patterns and interprets data through machine perception.",
    },
    "💻 Technology FAQs": {
        "What is Python?": "Python is a high-level, general-purpose programming language known for its simplicity and readability. It is widely used in AI, web development, data science, and automation.",
        "What is IoT?": "The Internet of Things (IoT) refers to the network of physical devices embedded with sensors, software, and connectivity to exchange data over the internet.",
        "What is Cloud Computing?": "Cloud computing delivers computing services — servers, storage, databases, networking, software — over the internet to offer faster innovation and flexible resources.",
        "What is Cybersecurity?": "Cybersecurity is the practice of protecting computers, networks, and data from unauthorized access, damage, or attacks using technologies and processes.",
        "What is a database?": "A database is an organized collection of structured information or data, typically stored electronically in a computer system and managed using a DBMS.",
        "What is an API?": "An Application Programming Interface (API) is a set of rules that allows one software application to interact with another, enabling integration and data exchange.",
    },
    "📡 ECE FAQs": {
        "What is ECE?": "Electronics and Communication Engineering (ECE) focuses on the design and development of electronic circuits, communication systems, signal processing, and embedded technologies.",
        "What subjects are taught in ECE?": "Core subjects include Digital Electronics, Signals & Systems, Communication Engineering, VLSI Design, Microprocessors, Embedded Systems, and Antenna Theory.",
        "What are the career options after ECE?": "ECE graduates can work in telecom, semiconductor, defense, embedded systems, IoT, and software companies. You can also pursue GATE for M.Tech or go into research.",
        "What is VLSI?": "Very Large Scale Integration (VLSI) is the process of creating an integrated circuit by combining millions of transistors onto a single chip, used in modern processors.",
        "What is Embedded Systems?": "Embedded Systems are dedicated computing systems performing specific functions within larger systems, like microcontrollers in washing machines, cars, and medical devices.",
        "What is 5G?": "5G is the 5th generation of mobile network technology offering faster speeds (up to 10 Gbps), lower latency, and greater capacity than 4G LTE.",
    },
}

flat_faq = {q: a for cat in faq_categories.values() for q, a in cat.items()}