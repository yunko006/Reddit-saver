import praw
import os

reddit = praw.Reddit(
    client_id="clientid here",
    client_secret="client secret here",
    user_agent="user agent here",
    username="username here",
    password="password here"
)

# nombre de post que l'on veux sauvegarder
n = 1000
# path ou on veux sauvegarder les fichiers
# exemple : "/Users/X/Documents/saved"
path = "your/path/here"


def create_path():
    """
    Créer un dossier la ou on veux sauvegarder nos fichiers
    """
    try:
        os.mkdir(path)
    except OSError:
        print(f"Creation of the Directory {path} failed")
    else:
        print(f"Successfully created the directory {path}")


def create_directory(name):
    """
    Créer des folders en fonction des noms des subreddits.
    Si un nom existe deja cela ne créer pas de doublons.
    """

    try:
        os.mkdir(f"{path}/{name}")
        print(f"Directory {name} created in {path}")
    except FileExistsError:
        pass


def get_title(item):
    """
    Fonction qui limite la taille pour le nom du fichier .txt
    si le nom du post est trop grand.
    """

    title = item.title
    # check la longueur du titre si trop: grand coupe le titre
    if len(title) >= 255:
        title = title[:250]

    return title


def main(n):
    # créer le dossier la ou on veux
    create_path()

    for item in reddit.user.me().saved(limit=n):
        # check si l'item est un post
        if isinstance(item, praw.models.Submission):

            # titre du post
            title = get_title(item)
            # nom du subreddit
            sub_name = item.subreddit.display_name
            # attribue le le titre du post subreddit à une variable.
            file_name = f"{title}.txt"

            # créer un folder avec le nom du subreddit
            create_directory(sub_name)

            # crée un fichier .txt dans le folder avec le nom du subreddit grâce à file_name
            filepath = os.path.join(
                f"{path}/{sub_name}", file_name)

            # # w+ pour le moment pour créer un fichier ou overwrite tout le test si le fichier est deja la
            try:
                # essaye de créer le fichier
                f = open(filepath, 'w+')
                # écrit le text du post dans le fichier.
                f.write(f"Autheur: {item.author}\n")
                f.write(f"\n{item.selftext}\n")
                f.write(f"\nLink to the post: reddit.com{item.permalink}")
                f.close()
            except OSError:
                # dans certains cas le fichier ne peux pas se créer. Affiche une erreur
                # et donne le lien du post.
                print(f"The file: {title} can not be created... ")
                print(
                    f"Here is the link to the post: reddit.com{item.permalink}\n")
                continue

        elif isinstance(item, praw.models.Comment):
            """
            Pb: va append le meme commentaire plusieurs fois si on rerun le script
            """
            # save tous les commentaires dans le même fichier.txt
            filename = 'comments.txt'
            dir_name = 'comments'

            create_directory(dir_name)

            file_path = os.path.join(f"{path}/{dir_name}", filename)

            f = open(file_path, 'a+')
            f.write(f"Commentaires from {item.subreddit}:\n")
            f.write(f"{item.body}\n\n")
            f.close()


if __name__ == "__main__":
    main(n)


############################################################
# def get_comment(n):

#     for item in reddit.user.me().saved(limit=n):
#         # attribuer l'id d'un post à submission
#         submission = reddit.submission(id=item.id)
#         # print les comments d'un post
#         # .list() pour pouvoir choisir le nombre de commentaire qu'on veux garder: ici 3
#         for top_level_comment in submission.comments.list()[:3]:
#             comments = top_level_comment.body

#         return comments
