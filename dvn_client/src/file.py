__author__="peterbull"
__date__ ="$Aug 16, 2013 12:32:24 PM$"

# python base lib modules
from datetime import datetime
import mimetypes

#downloaded modules
import sword2

#local modules
import utils


class DvnFile(object):
    def __init__(self, name, editMediaUri, mimetype, updated, hostStudy):
        self.name = name
        self.editMediaUri = editMediaUri
        self.mimetype = mimetype
        self.updated = updated
        self.hostStudy = hostStudy
        self.id = editMediaUri.split('/')[-2]
        
    def __repr__(self):
        return """
    DVN FILE:
    Name: {0}
    Uri: {1}
    Mime: {2}
    Id: {3}
    Status: DRAFT
    """.format(self.name, self.editMediaUri, self.mimetype, self.id)

    # Note: Information about files comes from the statement of the study, not the entry
    # # TODO untested!!!!!!!
    # @classmethod
    # def CreateFromAtomEntry(cls, atomXml, hostStudy):
    #     url = utils.get_elements(atomXml,
    #                                tag="id",
    #                                numberOfElements=1).text
    #
    #     name = url.rsplit("/")[-1]
    #     editMediaUri = url
    #
    #     contentType = utils.get_elements(atomXml,
    #                                tag="content",
    #                                numberOfElements=1).get("type")
    #     mimetype = mimetypes.guess_type(contentType)
    #
    #
    #     updatedString = utils.get_elements(atomXml,
    #                       tag="updated",
    #                       numberOfElements=1).text
    #     updated = datetime.utcfromtimestamp(updatedString)
    #     return cls(name, editMediaUri, mimetype, updated, hostStudy)
    #
    @classmethod
    def CreateFromAtomStatementObject(cls, atomStatementEntry, hostStudy):
        editMediaUri = atomStatementEntry.cont_iri
        name = editMediaUri.rsplit("/")[-1]
        mimetype = atomStatementEntry.content[editMediaUri]["type"]
        # Note: Updated element is meaningless at the moment
        updated = datetime.strptime(atomStatementEntry.updated, "%Y-%m-%dT%H:%M:%S.%fZ")
        return cls(name, editMediaUri, mimetype, updated, hostStudy)


class ReleasedFile(object):
    def __init__(self, name, uri, hostStudy):
        self.name = name
        self.uri = uri
        self.hostStudy = hostStudy
        self.id = uri.split('=')[-1]

    def __repr__(self):
        return """
    DVN FILE:
    Name: {0}
    Uri: {1}
    Id: {2}
    Status: RELEASED
    """.format(self.name, self.uri, self.id)