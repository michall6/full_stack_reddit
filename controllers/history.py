from databaseControllers.history import HistoryDBCtrl

class HistoryCtrl:
    @staticmethod
    def save_search(subreddit:str, category:str):
        try:
         HistoryDBCtrl.save_search_subreddit_category(subreddit,category)
            
        except Exception as e:
            print("/error in controllers save_search", e)


 