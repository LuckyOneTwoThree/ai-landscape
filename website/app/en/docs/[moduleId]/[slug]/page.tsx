import { getModules, getDocumentsInModule, getDocumentContent } from '@/lib/markdown'
import styles from '../../../../docs/[moduleId]/[slug]/markdown.module.css'
import Link from 'next/link'
import TableOfContents from '@/components/TableOfContents'

export async function generateStaticParams() {
  const modules = getModules('en')
  const paths = []
  
  for (const mod of modules) {
    const docs = getDocumentsInModule(mod.id, 'en')
    for (const doc of docs) {
      paths.push({
        moduleId: mod.id,
        slug: doc.slug,
      })
    }
  }
  
  return paths
}

type Params = Promise<{ moduleId: string, slug: string }>

export default async function DocumentPage({
  params
}: {
  params: Params
}) {
  const resolvedParams = await params;
  const { contentHtml, isFallback } = await getDocumentContent(resolvedParams.moduleId, resolvedParams.slug, 'en')
  
  return (
    <div className={styles.pageContainer}>
      <article className={styles.markdownBody}>
        {isFallback && (
          <blockquote style={{borderColor: '#eab308', color: '#eab308'}}>
            <strong>Translation Note:</strong> This article has not been translated into English yet. Falling back to the original Chinese version.
          </blockquote>
        )}

        <div dangerouslySetInnerHTML={{ __html: contentHtml }} />
      </article>
      <aside className={styles.tocAside}>
        <TableOfContents locale="en" />
      </aside>
    </div>
  )
}
