from datetime import datetime,timedelta
class CustomerComplaint:
    def __init__(self,category):
        self.category = category
        self.complaints = []
        self.category_priority = {'payment issue': 1, 'shipping delay': 2, 'other': 3}

    def submit_complaint(self,complaint):
        required_field = ['customer_type','category','timestamp']
        if not all(k in complaint for k in required_field):
            raise ValueError('Missing field')
        complaint['submitted'] = datetime.now()
        self.complaints.append(complaint)

    def get_next_complaint(self):
        escalation_threshold = timedelta(hours=2)
        now = datetime.now()

        def get_priority(c):
            is_vip = 0 if c['customer_type'].lower() == 'vip' else 1
            category_rank = self.category_priority.get(c['category'].lower(), 999)
            escalation = 0 if (now - c['submitted']) > escalation_threshold else 1
            return (is_vip, category_rank, escalation, c['timestamp'])
        
        if not self.complaints:
            return None
        
        sorted_complaint = sorted(self.complaints, key=get_priority)
        next_complaint = sorted_complaint[0]
        self.complaints.remove(next_complaint)
        return next_complaint
    
