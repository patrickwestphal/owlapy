from enum import Enum


class MissingImportHandlingStrategy(Enum):
    # Specifies that an owlapy.model.UnloadableImportException will NOT be
    # thrown during ontology loading if an import cannot be loaded (for what
    # ever reason). Instead, any registered
    # owlapy.model.MissingImportListener objects will be informed of the
    # problem via their
    # owlapy.model.MissingImportListener#importMissing(MissingImportEvent)
    # method.
    SILENT = 'silent'

    # Specifies that an owlapy.model.UnloadableImportException WILL be thrown
    # during ontology loading if an import cannot be loaded.
    THROW_EXCEPTION = 'throw_exception'
